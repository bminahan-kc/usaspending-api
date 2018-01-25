create index fabs_unique_id on transaction_fabs_new (afa_generated_unique);
create index fpds_unique_id on transaction_fpds_new (detached_award_proc_unique);
create index tx_unique_id on transaction_normalized_new (transaction_unique_id);

UPDATE transaction_fabs_new
SET transaction_id = tn_new.id
FROM transaction_normalized_new AS tn_new
WHERE tn_new.transaction_unique_id = transaction_fabs_new.afa_generated_unique;

UPDATE transaction_fpds_new
SET transaction_id = tn_new.id
FROM transaction_normalized_new AS tn_new
WHERE tn_new.transaction_unique_id = transaction_fpds_new.detached_award_proc_unique;

--UPDATE transaction_fabs_new
--SET transaction_id = (SELECT id FROM transaction_normalized_new WHERE transaction_normalized_new.transaction_unique_id = transaction_fabs_new.afa_generated_unique);
--
--UPDATE transaction_fpds_new
--SET transaction_id = (SELECT id FROM transaction_normalized_new WHERE transaction_normalized_new.transaction_unique_id = transaction_fpds_new.detached_award_proc_unique);