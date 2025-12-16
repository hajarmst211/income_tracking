#user_input.py

# Local function importation:
from  connection import connect 

# standard functions
import psycopg2
from decimal import Decimal
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def add_bank_account(connection,
                        rib,
                        bank_name,
                        current_balance,
                        account_type
                    ):
    try:
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


def add_transaction(connection,
                    money_amount,
                    transaction_reason,
                    account_id
                    ):
    try:
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


def add_expense_category(connection,
                        name,
                        description
                        ):
    try:
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


def add_monthly_expense(
                        connection,
                        expense_category,
                        amount,
                        due_day,
                        flexibility_degree
                        ):
    try:
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


def delete_bank_account(connection, account_id):
    try:
        with connection.cursor() as cursor:
            delete_script = '''
                DELETE FROM bank_account
                WHERE account_id = %s
            '''
            cursor.execute(delete_script, (account_id,))
            connection.commit()

        logging.info("Bank account deleted successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error deleting bank account: {error}")
        raise error


def delete_transaction(connection, transaction_id):
    try:
        with connection.cursor() as cursor:
            delete_script = '''
                DELETE FROM Transactions
                WHERE transaction_id = %s
            '''
            cursor.execute(delete_script, (transaction_id,))
            connection.commit()

        logging.info("Transaction deleted successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error deleting transaction: {error}")
        raise error


def delete_expense_category(connection, category_id):
    try:
        with connection.cursor() as cursor:
            delete_script = '''
                DELETE FROM expense_categories
                WHERE category_id = %s
            '''
            cursor.execute(delete_script, (category_id,))
            connection.commit()

        logging.info("Expense category deleted successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error deleting expense category: {error}")
        raise error


def delete_monthly_expense(connection, expense_id):
    try:
        with connection.cursor() as cursor:
            delete_script = '''
                DELETE FROM monthly_expenses
                WHERE expense_id = %s
            '''
            cursor.execute(delete_script, (expense_id,))
            connection.commit()

        logging.info("Monthly expense deleted successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error deleting monthly expense: {error}")
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