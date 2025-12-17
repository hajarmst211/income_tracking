#cli.py

#local functions:
from db_operations import add_bank_account, add_expense_category, add_monthly_expense, add_transaction
from db_operations import delete_bank_account, delete_expense_category, delete_transaction, delete_monthly_expense

#standard function:
from decimal import Decimal
import logging


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
        transaction_reason = input("Enter the reason for the transaction (e.g., Groceries, Salary): \n")
        account_id = int(input("Enter the ID of the bank account for this transaction: \n"))
        
        add_transaction(
                        connection,
                        money_amount,
                        transaction_reason,
                        account_id
                        )
        

def create_expense_category(connection):
        name = input("Enter the category name (e.g., Utilities, Entertainment): \n")
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
    account_id = int(input("Enter the account_id of the bank account to delete: \n"))
    delete_bank_account(connection, account_id)


def delete_transaction_cli(connection):
    transaction_id = int(input("Enter the transaction_id of the transaction to delete: \n"))
    delete_transaction(connection, transaction_id)
    

def delete_monthly_expense_cli(connection):
    category_id = int(input("Enter the category_id of the expense category to delete: \n"))
    delete_monthly_expense(connection, category_id)
    
    
def delete_expense_category_cli(connection):
    expense_id = int(input("Enter the expense_id of the monthly expense to delete: \n"))
    delete_expense_category(connection, expense_id)

    


def main_menu():
    choice_script = '''
                    Hi, welcome to your income tracking interface.
                    What type of transaction you want to make:
                    [1] Add a row
                    [2] Delete a row
                    [3] Display a table
                    [4] quit
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1,5):
            logging.error("The choice is out of range, it must be between 1 to 4")
    except ValueError :
        logging.error("Invalid value! Give an integer")
        
    return choice

def addition_menu():
    choice_script = '''
                    Hi, welcome to your income tracking interface.
                    What type of addition you want to do:
                    [1] Add Bank Account
                    [2] Add Transaction
                    [3] Add Expense Category
                    [4] Add monthly expense
                    [5] Back to main menu
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1,6):
            logging.error("The choice is out of range, it must be between 1 to 5")
    except ValueError :
        logging.error("Invalid value! Give an integer")
        
    return choice


def suppression_menu():
    choice_script = '''
                    Hi, welcome to your income tracking interface.
                    What type of suppression you want to do:
                    [1] delete Bank Account
                    [2] delete Transaction
                    [3] delete Expense Category
                    [4] delete monthly expense
                    [5] Back to main menu
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1,6):
            logging.error("The choice is out of range, it must be between 1 to 5")
    except ValueError :
        logging.error("Invalid value! Give an integer")
        
    return choice


def table_display_menu():
    choice_script = '''
                    Hi, welcome to your income tracking interface.
                    What table you want to display:
                    [1] Bank Account
                    [2] Transaction
                    [3] Expense Category
                    [4] monthly expense
                    [5] Back to main menu
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1,6):
            logging.error("The choice is out of range, it must be between 1 to 5")
    except ValueError :
        logging.error("Invalid value! Give an integer")
        
    return choice