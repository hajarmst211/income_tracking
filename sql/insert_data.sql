-- insert_data.sql

INSERT INTO users (username, first_name, last_name, password_hash) VALUES
('jdoe', 'John', 'Doe', 'pbkdf2:sha256:600000$randomhash');

INSERT INTO expense_categories (username, name, description) VALUES
('jdoe', 'Housing', 'Rent, mortgage, and property taxes'),
('jdoe', 'Utilities', 'Electricity, water, heating, and internet'),
('jdoe', 'Food', 'Groceries and dining out'),
('jdoe', 'Transportation', 'Fuel, public transit, and car maintenance'),
('jdoe', 'Entertainment', 'Streaming services, hobbies, and events'),
('jdoe', 'Health', 'Medical bills, pharmacy, and fitness'),
('jdoe', 'Insurance', 'Life, auto, and home insurance');

INSERT INTO bank_account (username, rib, bank_name, current_balance, account_type) VALUES
('jdoe', '12345678901234567890', 'Chase Bank', 4520.50, 'checking'),
('jdoe', '98765432109876543210', 'Bank of America', 0.00, 'savings'),
('jdoe', '11223344556677889900', 'Wells Fargo', 50000.00, 'deposit'),
('jdoe', '55667788990011223344', 'Ally Bank', 850.75, 'checking');

INSERT INTO monthly_expenses (username, expense_category, amount, due_day, flexibility_degree) VALUES
('jdoe', 1, 1500.00, 1, '0'),
('jdoe', 2, 120.00, 15, '1'),
('jdoe', 2, 45.00, 20, '1'),
('jdoe', 3, 400.00, 5, '2'),
('jdoe', 4, 350.00, 10, '1'),
('jdoe', 5, 15.99, 12, '1'),
('jdoe', 6, 60.00, 1, '2'),
('jdoe', 3, 150.00, 25, '3');

INSERT INTO Transactions (username, account_id, money_amount, transaction_reason, transaction_date) VALUES
('jdoe', 1, 3200.00, 'Salary Deposit', '2023-10-01 09:00:00'),
('jdoe', 1, -1500.00, 'Rent Payment October', '2023-10-01 10:30:00'),
('jdoe', 1, -45.20, 'Grocery Store', '2023-10-03 14:15:00'),
('jdoe', 1, -15.99, 'Netflix Subscription', '2023-10-12 08:00:00'),
('jdoe', 1, -60.00, 'Gas Station', '2023-10-15 18:45:00'),
('jdoe', 1, -120.00, 'Electric Bill', '2023-10-15 19:00:00'),
('jdoe', 1, 50.00, 'Birthday Gift (Mom)', '2023-10-20 12:00:00'),
('jdoe', 1, -85.50, 'Restaurant Dinner', '2023-10-21 20:30:00'),
('jdoe', 1, -12.50, 'Coffee Shop', '2023-10-22 08:15:00'),
('jdoe', 1, -350.00, 'Car Loan Payment', '2023-10-25 10:00:00');