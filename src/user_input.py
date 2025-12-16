#user_input.py

# Local function importation:
from  connection import connect 

# standard functions
import psycopg2
from decimal import Decimal
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def add_bank_account(connection):
    try:
        rib = Decimal(input("Enter your rib: \n"))
        bank_name = input("what is the bank's name: \n")
        current_balance = Decimal(input("what is the current balance?: \n"))
        account_type = input("what is the account's type?: \n")
         
        with connection.cursor() as cursor:
            insert_script = '''
                            INSERT INTO bank_account (
                                rib,
                                bank_name,
                                current_balance,
                                account_type
                                )
                            VALUES (%s, %s, %s, %s)
                            '''
            cursor.execute(insert_script, (rib, bank_name, current_balance, account_type))
            connection.commit()
            
        logging.info("bank account added successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        raise error


def add_transaction(connection):
    try:
        money_amount = Decimal(input("Enter the transaction amount: \n"))
        transaction_reason = input("Enter the reason for the transaction (e.g., Groceries, Salary): \n")
        account_id = int(input("Enter the ID of the bank account for this transaction: \n"))
         
        with connection.cursor() as cursor:
            insert_script = '''
                            INSERT INTO Transactions (
                                money_amount,
                                transaction_reason,
                                account_id
                                )
                            VALUES (%s, %s, %s)
                            '''
            cursor.execute(insert_script, (money_amount, transaction_reason, account_id))
            connection.commit()
            
        logging.info("Transaction added successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error adding transaction: {error}")
        raise error


def add_expense_category(connection):
    try:
        name = input("Enter the category name (e.g., Utilities, Entertainment): \n")
        description = input("Enter a brief description for this category (optional): \n")
         
        with connection.cursor() as cursor:
            insert_script = '''
                            INSERT INTO expense_categories (
                                name,
                                description
                                )
                            VALUES (%s, %s)
                            '''
            cursor.execute(insert_script, (name, description))
            connection.commit()

        logging.info("Expense category added successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error adding expense category: {error}")
        raise error


def add_monthly_expense(connection):
    try:
        expense_category = input("Provide an expense_category (category_id): \n")
        amount = Decimal(input("Provide the amount: \n"))
        due_day = Decimal(input("Provide the due day (1–31): \n"))
        flexibility_degree = Decimal(input("Provide the flexibility degree: \n"))

        with connection.cursor() as cursor:
            insert_script = '''
                INSERT INTO monthly_expenses (
                    expense_category,
                    amount,
                    due_day,
                    flexibility_degree
                )
                VALUES (%s, %s, %s, %s)
            '''

            cursor.execute(
                insert_script,
                (expense_category, amount, due_day, flexibility_degree)
            )
            connection.commit()

        logging.info("bank monthly expense added successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        raise error



if __name__ == "__main__":
    try:
        connection =  connect()
        if connection is not  None:
            add_bank_account(connection)
            add_transaction(connection)
            add_monthly_expense(connection)
            add_expense_category(connection)
            
            
            
        
    except Exception as error:
        logging.error(error)
        if connection:
            connection.rollback()
    
    finally:
        if connection:
            connection.close()
            
    