import numpy as np
import pandas as pd

from collections import deque
from django.db import connections
from django.utils.functional import cached_property
from usaspending_api.references.models import ObjectClass, RefProgramActivity


class Bunch:
    """Generic class to hold a group of attributes."""

    def __init__(self, **kwds):
        self.__dict__.update(kwds)


def get_or_create_program_activity(row, submission_attributes):
    # We do it this way rather than .get_or_create because we do not want to duplicate existing pk's with null values
    filters = {
        "program_activity_code": row["program_activity_code"],
        "program_activity_name": row["program_activity_name"].upper()
        if row["program_activity_name"]
        else row["program_activity_name"],
        "budget_year": submission_attributes.reporting_fiscal_year,
        "responsible_agency_id": row["agency_identifier"],
        "allocation_transfer_agency_id": row["allocation_transfer_agency"],
        "main_account_code": row["main_account_code"],
    }
    prg_activity = RefProgramActivity.objects.filter(**filters).first()
    if prg_activity is None and row["program_activity_code"] is not None:
        # If the PA has a blank name, create it with the value in the row.
        # PA loader should overwrite the names for the unique PAs from the official
        # domain values list if the title needs updating, but for now grab it from the submission
        prg_activity = RefProgramActivity.objects.create(**filters)
        # logger.warning('Created missing program activity record for {}'.format(str(filters)))

    return prg_activity


def get_object_class_row(row):
    """Lookup an object class record.

       (As ``get_object_class``, but arguments are bunched into a ``row`` object.)

        Args:
            row.object_class: object class from the broker
            row.by_direct_reimbursable_fun: direct/reimbursable flag from the broker
                (used only when the object_class is 3 digits instead of 4)
    """

    # Object classes are numeric strings so let's ensure the one we're passed is actually a string before we begin.
    object_class = str(row.object_class).zfill(3) if type(row.object_class) is int else row.object_class

    # As per DEV-4030, "000" object class is a special case due to common spreadsheet mangling issues.  If
    # we receive an object class that is all zeroes, convert it to "000".  This also handles the special
    # case of "0000".
    if object_class is not None and object_class == "0" * len(object_class):
        object_class = "000"

    # Alias this to cut down on line lengths a little below.
    ocdr = ObjectClass.DIRECT_REIMBURSABLE

    if len(object_class) == 4:
        # this is a 4 digit object class, 1st digit = direct/reimbursable information
        direct_reimbursable = ocdr.LEADING_DIGIT_MAPPING[object_class[0]]
        object_class = object_class[1:]
    else:
        # the object class field is the 3 digit version, so grab direct/reimbursable information from a separate field
        try:
            direct_reimbursable = ocdr.BY_DIRECT_REIMBURSABLE_FUN_MAPPING[row.by_direct_reimbursable_fun]
        except KeyError:
            # So Broker sort of validates this data, but not really.  It warns submitters that their data
            # is bad but doesn't force them to actually fix it.  As such, we are going to just ignore
            # anything we do not recognize.  Terrible solution, but it's what we've been doing to date
            # and I don't have a better one.
            direct_reimbursable = None

    # This will throw an exception if the object class does not exist which is the new desired behavior.
    try:
        return ObjectClass.objects.get(object_class=object_class, direct_reimbursable=direct_reimbursable)
    except ObjectClass.DoesNotExist:
        raise ObjectClass.DoesNotExist(
            f"Unable to find object class for object_class={object_class}, direct_reimbursable={direct_reimbursable}."
        )


def get_object_class(row_object_class, row_direct_reimbursable):
    """Lookup an object class record.

        Args:
            row_object_class: object class from the broker
            row_direct_reimbursable: direct/reimbursable flag from the broker
                (used only when the object_class is 3 digits instead of 4)
    """

    row = Bunch(object_class=row_object_class, by_direct_reimbursable_fun=row_direct_reimbursable)
    return get_object_class_row(row)


class CertifiedAwardFinancialIterator:
    chunk_size = 100000

    def __init__(self, submission_attributes):
        self.submission_attributes = submission_attributes

        # For managing state.
        self._last_id = None
        self._current_chunk = None

    def _retrieve_and_prepare_next_chunk(self):
        sql = f"""
            select  *
            from    certified_award_financial
            where   submission_id = {self.submission_attributes.broker_submission_id} and
                    {"" if self._last_id is None else f"certified_award_financial_id > {self._last_id} and"}
                    transaction_obligated_amou is not null and
                    transaction_obligated_amou != 0
            order   by certified_award_financial_id
            limit   {self.chunk_size}
        """

        award_financial_frame = pd.read_sql(sql, connections["data_broker"])

        if award_financial_frame.size > 0:
            award_financial_frame["object_class"] = award_financial_frame.apply(get_object_class_row, axis=1)
            award_financial_frame["program_activity"] = award_financial_frame.apply(
                get_or_create_program_activity, axis=1, submission_attributes=self.submission_attributes
            )
            award_financial_frame = award_financial_frame.replace({np.nan: None})

            self._last_id = award_financial_frame["certified_award_financial_id"].max()
            self._current_chunk = deque(award_financial_frame.to_dict(orient="records"))

        else:
            self._last_id = None
            self._current_chunk = None

    def __next__(self):
        if not self._current_chunk:
            self._retrieve_and_prepare_next_chunk()
            if not self._current_chunk:
                raise StopIteration
        return self._current_chunk.popleft()


class CertifiedAwardFinancial:
    """ Abstract away the messy details of how we retrieve and prepare certified_award_financial rows. """

    def __init__(self, submission_attributes):
        self.submission_attributes = submission_attributes

    @cached_property
    def count(self):
        sql = f"""
            select  count(*)
            from    certified_award_financial
            where   submission_id = {self.submission_attributes.broker_submission_id} and
                    transaction_obligated_amou is not null and
                    transaction_obligated_amou != 0
        """
        with connections["data_broker"].cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()[0][0]

    def __iter__(self):
        return CertifiedAwardFinancialIterator(self.submission_attributes)
