DROP VIEW IF EXISTS award_delta_view;

CREATE VIEW award_delta_view AS
SELECT
  vw_award_search.award_id,
  a.generated_unique_award_id,
    CASE
    WHEN vw_award_search.type IN ('02', '03', '04', '05', '06', '10', '07', '08', '09', '11') AND vw_award_search.fain IS NOT NULL THEN vw_award_search.fain
    WHEN vw_award_search.piid IS NOT NULL THEN vw_award_search.piid  -- contracts. Did it this way to easily handle IDV contracts
    ELSE vw_award_search.uri
  END AS display_award_id,

  vw_award_search.category,
  vw_award_search.type,
  vw_award_search.type_description,
  vw_award_search.piid,
  vw_award_search.fain,
  vw_award_search.uri,
  vw_award_search.total_obligation,
  vw_award_search.description,
  vw_award_search.award_amount,
  vw_award_search.total_subsidy_cost,
  vw_award_search.total_loan_value,
  a.update_date,

  vw_award_search.recipient_name,
  vw_award_search.recipient_unique_id,
  recipient_lookup.recipient_hash,
  vw_award_search.parent_recipient_unique_id,
  vw_award_search.business_categories,

  vw_award_search.action_date,
  vw_award_search.fiscal_year,
  vw_award_search.last_modified_date,
  vw_award_search.period_of_performance_start_date,
  vw_award_search.period_of_performance_current_end_date,
  vw_award_search.date_signed,
  vw_award_search.ordering_period_end_date,

  vw_award_search.original_loan_subsidy_cost,
  vw_award_search.face_value_loan_guarantee,

  vw_award_search.awarding_agency_id,
  vw_award_search.funding_agency_id,
  vw_award_search.awarding_toptier_agency_name,
  vw_award_search.funding_toptier_agency_name,
  vw_award_search.awarding_subtier_agency_name,
  vw_award_search.funding_subtier_agency_name,
  vw_award_search.awarding_toptier_agency_code,
  vw_award_search.funding_toptier_agency_code,
  vw_award_search.awarding_subtier_agency_code,
  vw_award_search.funding_subtier_agency_code,

  vw_award_search.recipient_location_country_code,
  vw_award_search.recipient_location_country_name,
  vw_award_search.recipient_location_state_code,
  vw_award_search.recipient_location_county_code,
  vw_award_search.recipient_location_county_name,
  vw_award_search.recipient_location_congressional_code,
  vw_award_search.recipient_location_zip5,
  vw_award_search.recipient_location_city_name,

  vw_award_search.pop_country_code,
  vw_award_search.pop_country_name,
  vw_award_search.pop_state_code,
  vw_award_search.pop_county_code,
  vw_award_search.pop_county_name,
  vw_award_search.pop_zip5,
  vw_award_search.pop_congressional_code,
  vw_award_search.pop_city_name,
  vw_award_search.pop_city_code,

  vw_award_search.cfda_number,
  vw_award_search.sai_number,
  vw_award_search.type_of_contract_pricing,
  vw_award_search.extent_competed,
  vw_award_search.type_set_aside,

  vw_award_search.product_or_service_code,
  vw_award_search.product_or_service_description,
  vw_award_search.naics_code,
  vw_award_search.naics_description,
  TREASURY_ACCT.tas_paths,
  TREASURY_ACCT.tas_components
FROM vw_award_search
INNER JOIN awards a ON (a.id = vw_award_search.award_id)
LEFT JOIN (
  SELECT
    recipient_hash,
    legal_business_name AS recipient_name,
    duns
  FROM
    recipient_lookup AS rlv
) recipient_lookup ON (recipient_lookup.duns = vw_award_search.recipient_unique_id AND vw_award_search.recipient_unique_id IS NOT NULL)
LEFT JOIN (
  SELECT
    faba.award_id,
    ARRAY_AGG(
      DISTINCT CONCAT(
        'agency=', agency.toptier_code,
        'faaid=', fa.agency_identifier,
        'famain=', fa.main_account_code,
        'aid=', taa.agency_id,
        'main=', taa.main_account_code,
        'ata=', taa.allocation_transfer_agency_id,
        'sub=', taa.sub_account_code,
        'bpoa=', taa.beginning_period_of_availability,
        'epoa=', taa.ending_period_of_availability,
        'a=', taa.availability_type_code
       )
     ) tas_paths,
     ARRAY_AGG(
      DISTINCT CONCAT(
        'aid=', taa.agency_id,
        'main=', taa.main_account_code,
        'ata=', taa.allocation_transfer_agency_id,
        'sub=', taa.sub_account_code,
        'bpoa=', taa.beginning_period_of_availability,
        'epoa=', taa.ending_period_of_availability,
        'a=', taa.availability_type_code
       )
     ) tas_components
 FROM
   treasury_appropriation_account taa
   INNER JOIN financial_accounts_by_awards faba ON (taa.treasury_account_identifier = faba.treasury_account_id)
   INNER JOIN federal_account fa ON (taa.federal_account_id = fa.id)
   INNER JOIN toptier_agency agency ON (fa.parent_toptier_agency_id = agency.toptier_agency_id)
 WHERE
   faba.award_id IS NOT NULL
 GROUP BY
   faba.award_id
) TREASURY_ACCT ON (TREASURY_ACCT.award_id = vw_award_search.award_id);
