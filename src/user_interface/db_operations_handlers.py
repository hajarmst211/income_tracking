# db_operations_handlers.py

#local functions:
from database.repository import add_bank_account, add_expense_category, add_monthly_expense, add_transaction, add_user
from database.repository import delete_bank_account, delete_expense_category, delete_transaction, delete_monthly_expense
from database.repository import get_all_records
from user_interface.menus import signup_menu

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
    

def display_table(connection, table_name):
    headers, rows = get_all_records(connection, table_name)
    
    print(f"\nDisplaying Table: {table_name}")
    print_as_table(headers, rows)


def create_bank_account(connection):    
    rib = Decimal(input("Enter your rib: \n"))
    bank_name = input("what is the bank's name: \n")
    balance = Decimal(input("what is the current balance?: \n"))
    account_type = input("what is the account's type?: \n")
        
    add_bank_account(
        connection,
        rib=rib,
        bank_name=bank_name,
        current_balance=balance,
        account_type=account_type
    )


def create_transaction(connection):
        money_amount = Decimal(input("Enter the transaction amount: \n"))
        transaction_reason = input("Enter the reason for the transaction: \n")
        account_id = int(input("Enter the ID of the bank account for this transaction: \n"))
        
        add_transaction(
                        connection,
                        money_amount,
                        transaction_reason,
                        account_id
                        )
        

def create_expense_category(connection):
        name = input("Enter the category name: \n")
        description = input("Enter a brief description for this category (optional): \n")
        
        add_expense_category(
                            connection,
                            name,
                            description
                            )
         
def create_monthly_expense(connection):
    expense_category = input("Provide an expense_category (category_id): \n")
    amount = Decimal(input("Provide the amount: \n"))
    due_day = Decimal(input("Provide the due day (1–31): \n"))
    flexibility_degree = Decimal(input("Provide the flexibility degree: \n"))

    add_monthly_expense(
                        connection,
                        expense_category,
                        amount,
                        due_day,
                        flexibility_degree
                        )       
    

def delete_bank_account_cli(connection):
    print("This is an overview of the bank accounts table:\n")
    display_table(connection, 'bank_account')
    account_id = int(input("Enter the account_id of the bank account to delete: \n"))
    delete_bank_account(connection, account_id)


def delete_transaction_cli(connection):
    print("This is an overview of the transactions table:\n")
    display_table(connection, 'Transactions')
    transaction_id = int(input("Enter the transaction_id of the transaction to delete: \n"))
    delete_transaction(connection, transaction_id)
    

def delete_monthly_expense_cli(connection):
    print("This is an overview of the monthly_expenses table:\n")
    display_table(connection, 'monthly_expenses')
    category_id = int(input("Enter the category_id of the expense category to delete: \n"))
    delete_monthly_expense(connection, category_id)
    
    
def delete_expense_category_cli(connection):
    try:
        print("This is an overview of the expense_categories table:\n")
        display_table(connection, 'expense_categories')
        expense_id = int(input("Enter the expense_id of the monthly expense to delete: \n"))
        delete_expense_category(connection, expense_id)
    except Exception as error:
        logging.error(error)
        
def create_user_cli(connection):
        # username:
        username = input("Choose a username (max 10 characters):\n").strip()
        if not username:
            logging.error("Error: Username cannot be empty.\n")
            return signup_menu()
        if len(username) > 10:
            print("Error: Username exceeds the 10-character limit.\n")
            return signup_menu()
        
        # first name:
        first_name = input("Enter your first name:\n").strip()
        if not first_name or len(first_name) > 20:
            logging.error("Error: First name must be between 1 and 20 characters.\n")
            return signup_menu()

        # last name:
        last_name = input("Enter your last name:\n").strip()
        if not last_name or len(last_name) > 20:
            logging.error("Error: Last name must be between 1 and 20 characters.\n")
            return signup_menu()

        # password
        password = input("Enter a password:\n")
        if not password:
            logging.error("Error: Password cannot be empty.\n")
            return signup_menu()
        
        # confirm password!  
        confirm_password = input("Confirm your password:\n")
        if password != confirm_password:
            logging.error("Error: Passwords do not match.\n")
            return signup_menu()

        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        
        # add user:
        user = add_user(username, first_name, last_name, hashed_password)
        return 0
        
        