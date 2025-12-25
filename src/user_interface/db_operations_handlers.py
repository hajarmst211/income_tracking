# db_operations_handlers.py

# local functions:
from src.database.repository import *

#standard function:
from decimal import Decimal
from prettytable import PrettyTable
import logging
import bcrypt

def print_as_table(headers, rows):
    if not rows:
        print("\nNo data found in this table \n")
        return

    table = PrettyTable()
    table.field_names = headers
    table.add_rows(rows)
    table.align = "c"
    print(table)
    
'''    
    while hajar.isAlive() {
        anas.love(hajar).forever()
        hajar.love(anas).back()
    }
'''
    

def display_table(connection, table_name, username):
    headers, rows = get_all_records(connection, table_name, username)
    print(f"\nDisplaying Table: {table_name}")
    print_as_table(headers, rows)

def create_bank_account(connection, username):    
    rib = input("Enter your rib: \n")
    bank_name = input("what is the bank's name: \n")
    balance = Decimal(input("what is the current balance?: \n"))
    account_type = input("what is the account's type (savings, deposit, checking)?: \n")
        
    add_bank_account(
        connection,
        username,
        rib=rib,
        bank_name=bank_name,
        current_balance=balance,
        account_type=account_type
    )

def create_transaction(connection, username):
    money_amount = Decimal(input("Enter the transaction amount: \n"))
    transaction_reason = input("Enter the reason for the transaction: \n")
    account_id = int(input("Enter the ID of the bank account for this transaction: \n"))
    
    add_transaction(
        connection,
        username,
        money_amount,
        transaction_reason,
        account_id
    )

def create_expense_category(connection, username):
    name = input("Enter the category name: \n")
    description = input("Enter a brief description for this category (optional): \n")
    
    add_expense_category(
        connection,
        username,
        name,
        description
    )
         
def create_monthly_expense(connection, username):
    expense_category = int(input("Provide the category_id: \n"))
    amount = Decimal(input("Provide the amount: \n"))
    due_day = int(input("Provide the due day (1–31): \n"))
    flexibility_degree = input("Provide the flexibility degree (0, 1, 2, 3): \n")

    add_monthly_expense(
        connection,
        username,
        expense_category,
        amount,
        due_day,
        flexibility_degree
    )       

def delete_bank_account_cli(connection, username):
    print("This is an overview of your bank accounts:\n")
    display_table(connection, 'bank_account', username)
    account_id = int(input("Enter the account_id to delete: \n"))
    delete_bank_account(connection, username, account_id)

def delete_transaction_cli(connection, username):
    print("This is an overview of your transactions:\n")
    display_table(connection, 'Transactions', username)
    transaction_id = int(input("Enter the transaction_id to delete: \n"))
    delete_transaction(connection, username, transaction_id)

def delete_monthly_expense_cli(connection, username):
    print("This is an overview of your monthly expenses:\n")
    display_table(connection, 'monthly_expenses', username)
    expense_id = int(input("Enter the expense_id to delete: \n"))
    delete_monthly_expense(connection, username, expense_id)
    
def delete_expense_category_cli(connection, username):
    try:
        print("This is an overview of your expense categories:\n")
        display_table(connection, 'expense_categories', username)
        category_id = int(input("Enter the category_id to delete: \n"))
        delete_expense_category(connection, username, category_id)
    except Exception as error:
        logging.error(error)
        
def create_user_cli(connection):
    username = input("Choose a username (max 10 characters):\n").strip()
    if not username or len(username) > 10:
        logging.error("Invalid username.")
        return
    
    first_name = input("Enter your first name:\n").strip()
    last_name = input("Enter your last name:\n").strip()
    password = input("Enter a password:\n")
    confirm_password = input("Confirm your password:\n")

    if password != confirm_password:
        logging.error("Passwords do not match.")
        return

    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt).decode('utf-8')
    
    return add_user(connection, username, first_name, last_name, hashed_password)
    