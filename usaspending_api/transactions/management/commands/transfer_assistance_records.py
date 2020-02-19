from django.core.management.base import BaseCommand

from usaspending_api.transactions.agnostic_transaction_loader import AgnosticTransactionLoader
from usaspending_api.transactions.models.source_assistance_transaction import SourceAssistanceTransaction


class Command(AgnosticTransactionLoader, BaseCommand):
    help = "Upsert assistance transactions from a Broker database into an USAspending database"
    broker_source_table_name = SourceAssistanceTransaction().broker_source_table
    delete_management_command = "delete_assistance_records"
    destination_table_name = SourceAssistanceTransaction().table_name
    extra_predicate = [{"field": "is_active", "op": "EQUAL", "value": "true"}]
    last_load_record = "source_assistance_transaction"
    lookback_minutes = 15
    shared_pk = "afa_generated_unique"
    working_file_prefix = "assistance_load_ids"
    broker_full_select_sql = 'SELECT "{id}" FROM "{table}" WHERE "is_active" IS TRUE'
    broker_incremental_select_sql = """
SELECT "{id}"
FROM   "{table}"
WHERE
  "is_active" IS TRUE
  AND
    "submission_id" IN (
      SELECT "submission_id"
      FROM   "submission"
      WHERE
        "d2_submission" IS TRUE
        AND "publish_status_id" IN (2, 3)
        {optional_predicate}
  )
"""
