-- 03_test_query.sql

BEGIN;

SELECT t.transaction_reason, t.money_amount, b.bank_name
FROM Transactions AS t
JOIN bank_account AS b ON t.account_id = b.account_id
GROUP BY t.transaction_reason, t.money_amount, b.bank_name
;

ROLLBACK;