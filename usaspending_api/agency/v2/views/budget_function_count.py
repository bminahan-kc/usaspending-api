from django.db.models import Exists, OuterRef
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any
from usaspending_api.accounts.models import TreasuryAppropriationAccount
from usaspending_api.agency.v2.views.agency_base import AgencyBase
from usaspending_api.common.cache_decorator import cache_response
from usaspending_api.financial_activities.models import FinancialAccountsByProgramActivityObjectClass


class BudgetFunctionCount(AgencyBase):
    """
    Obtain the count of budget functions for a specific agency in a single
    fiscal year based on whether or not that budget function has ever
    been submitted in File B.
    """

    endpoint_doc = "usaspending_api/api_contracts/contracts/v2/agency/toptier_code/budget_function/count.md"

    @cache_response()
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        rows = list(self.get_budget_function_queryset())

        return Response(
            {
                "toptier_code": self.toptier_code,
                "fiscal_year": self.fiscal_year,
                "budget_function_count": len(set([row["budget_function_code"] for row in rows])),
                "budget_sub_function_count": len(set([row["budget_subfunction_code"] for row in rows])),
                "messages": self.standard_response_messages,
            }
        )

    def get_budget_function_queryset(self):
        return (
            TreasuryAppropriationAccount.objects.annotate(
                include=Exists(
                    FinancialAccountsByProgramActivityObjectClass.objects.filter(
                        treasury_account_id=OuterRef("pk"),
                        final_of_fy=True,
                        treasury_account__funding_toptier_agency=self.toptier_agency,
                        submission__reporting_fiscal_year=self.fiscal_year,
                    ).values("pk")
                )
            )
            .filter(include=True)
            .values("budget_function_code", "budget_subfunction_code")
        )
