--01_create_tables.sql

CREATE TYPE account_types AS ENUM ('savings', 'deposit', 'checking');
CREATE TYPE flexibility_levels AS ENUM ('0', '1', '2', '3');


CREATE TABLE IF NOT EXISTS bank_account(
    account_id SERIAL PRIMARY KEY,
    rib VARCHAR(20),
    bank_name VARCHAR(20),
    current_balance NUMERIC(12, 2),
    account_type account_types
);


CREATE TABLE IF NOT EXISTS Transactions(
    transaction_id SERIAL PRIMARY KEY,
    money_amount NUMERIC(12, 2) NOT NULL,
    transaction_reason VARCHAR(225),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    account_id INT REFERENCES bank_account(account_id)
);


CREATE TABLE If NOT EXISTS expense_categories(
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    description TEXT
);


CREATE TABLE IF NOT EXISTS monthly_expenses(
    expense_id SERIAL PRIMARY KEY,
    expense_category INT REFERENCES expense_categories(category_id),
    amount NUMERIC(12, 2),
    due_day INT CHECK (due_day BETWEEN 1 AND 31),
    flexibility_degree flexibility_levels
);
