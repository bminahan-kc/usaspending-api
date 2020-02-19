import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connections

from usaspending_api.broker.helpers.store_deleted_fabs import store_deleted_fabs
from usaspending_api.transactions.agnostic_transaction_deletes import AgnosticDeletes
from usaspending_api.transactions.models.source_assistance_transaction import SourceAssistanceTransaction

logger = logging.getLogger("script")


class Command(AgnosticDeletes, BaseCommand):
    help = "Delete assistance transactions in an USAspending database"
    destination_table_name = SourceAssistanceTransaction().table_name
    shared_pk = "published_award_financial_assistance_id"

    def fetch_deleted_transactions(self, date):
        if settings.IS_LOCAL:
            logger.info("Local mode does not handle deleted records")
            return None

        sql = """
        select  published_award_financial_assistance_id
        from    published_award_financial_assistance p
        where   correction_delete_indicatr = 'D' and
                not exists (
                    select  *
                    from    published_award_financial_assistance
                    where   afa_generated_unique = p.afa_generated_unique and is_active is true
                )
                and updated_at >= %s
        """
        with connections["data_broker"].cursor() as cursor:
            cursor.execute(sql, [date])
            results = cursor.fetchall()
            return {date: [row[0] for row in results]} if results else None

    def store_delete_records(self, id_list):
        """FABS needs to store IDs for downline ETL, run that here"""
        store_deleted_fabs(id_list)
