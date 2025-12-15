--2_insert_data.sql


INSERT INTO expense_categories (name, description) VALUES
    ('Housing', 'Rent, mortgage, and property taxes'),
    ('Utilities', 'Electricity, water, heating, and internet'),
    ('Food', 'Groceries and dining out'),
    ('Transportation', 'Fuel, public transit, and car maintenance'),
    ('Entertainment', 'Streaming services, hobbies, and events'),
    ('Health', 'Medical bills, pharmacy, and fitness'),
    ('Insurance', 'Life, auto, and home insurance');

INSERT INTO bank_account (rib, bank_name, current_balance, account_type) VALUES
    ('12345678901234567890', 'Chase Bank', 4520.50, 'checking'),
    ('98765432109876543210', 'Bank of America', 12000.00, 'savings'),
    ('11223344556677889900', 'Wells Fargo', 50000.00, 'deposit'),
    ('55667788990011223344', 'Ally Bank', 850.75, 'checking');


-- Flexibility: '0' = Fixed (Rent), '3' = Highly Flexible (Dining out budget)
INSERT INTO monthly_expenses (expense_category, amount, due_day, flexibility_degree) VALUES
    (1, 1500.00, 1, '0'),  -- Housing (Rent)
    (2, 120.00, 15, '1'), -- Utilities (Internet/Elec)
    (2, 45.00, 20, '1'),  -- Utilities (Water)
    (3, 400.00, 5, '2'),  -- Food (Groceries Budget)
    (4, 350.00, 10, '1'), -- Transportation (Car Payment)
    (5, 15.99, 12, '1'),  -- Entertainment (Netflix)
    (6, 60.00, 1, '2'),   -- Health (Gym Membership)
    (3, 150.00, 25, '3'); -- Food (Dining Out)


INSERT INTO Transactions (money_amount, transaction_reason, transaction_date) VALUES
    (3200.00, 'Salary Deposit', '2023-10-01 09:00:00'),
    (-1500.00, 'Rent Payment October', '2023-10-01 10:30:00'),
    (-45.20, 'Grocery Store', '2023-10-03 14:15:00'),
    (-15.99, 'Netflix Subscription', '2023-10-12 08:00:00'),
    (-60.00, 'Gas Station', '2023-10-15 18:45:00'),
    (-120.00, 'Electric Bill', '2023-10-15 19:00:00'),
    (50.00, 'Birthday Gift (Mom)', '2023-10-20 12:00:00'),
    (-85.50, 'Restaurant Dinner', '2023-10-21 20:30:00'),
    (-12.50, 'Coffee Shop', '2023-10-22 08:15:00'),
    (-350.00, 'Car Loan Payment', '2023-10-25 10:00:00');