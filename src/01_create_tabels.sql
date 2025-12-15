CREATE TYPE account_types AS ENUM ('savings', 'deposit', 'checking');

CREATE TABLE IF NOT EXISTS account(
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(5),
    balance INT,
    account_type account_types
);

