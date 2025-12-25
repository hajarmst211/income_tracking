# repository.py

# local function
from connection import connect 

# standard libraries
import psycopg2
from psycopg2 import sql
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_all_records(connection, table_name, username):
    try:
        with connection.cursor() as cursor:
            query = sql.SQL("SELECT * FROM {table} WHERE username = %s").format(
                table=sql.Identifier(table_name)
            )
            cursor.execute(query, (username,))
            headers = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            return headers, rows
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        raise error

def add_bank_account(connection, username, rib, bank_name, current_balance, account_type):
    try:
        with connection.cursor() as cursor:
            insert_script = '''
                INSERT INTO bank_account (username, rib, bank_name, current_balance, account_type)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING *;
            '''
            cursor.execute(insert_script, (username, rib, bank_name, current_balance, account_type))
            new_account = cursor.fetchone()
            connection.commit()
            logging.info("Bank account added successfully!")
            return new_account
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        connection.rollback()
        raise error

def add_transaction(connection, username, money_amount, transaction_reason, account_id):
    try:
        with connection.cursor() as cursor:
            insert_script = '''
                INSERT INTO Transactions (username, money_amount, transaction_reason, account_id)
                VALUES (%s, %s, %s, %s)
                RETURNING *;
            '''
            cursor.execute(insert_script, (username, money_amount, transaction_reason, account_id))
            new_transaction = cursor.fetchone()
            connection.commit()
            logging.info("Transaction added successfully!")
            return new_transaction
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error adding transaction: {error}")
        connection.rollback()
        raise error

def add_expense_category(connection, username, name, description):
    try:
        with connection.cursor() as cursor:
            insert_script = '''
                INSERT INTO expense_categories (username, name, description)
                VALUES (%s, %s, %s)
                RETURNING *;
            '''
            cursor.execute(insert_script, (username, name, description))
            new_category = cursor.fetchone()
            connection.commit()
            logging.info("Expense category added successfully!")
            return new_category
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error adding expense category: {error}")
        connection.rollback()
        raise error

def add_monthly_expense(connection, username, expense_category, amount, due_day, flexibility_degree):
    try:
        with connection.cursor() as cursor:
            insert_script = '''
                INSERT INTO monthly_expenses (username, expense_category, amount, due_day, flexibility_degree)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING *;
            '''
            cursor.execute(insert_script, (username, expense_category, amount, due_day, flexibility_degree))
            new_expense = cursor.fetchone()
            connection.commit()
            logging.info("Monthly expense added successfully!")
            return new_expense
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        connection.rollback()
        raise error

def delete_bank_account(connection, username, account_id):
    try:
        with connection.cursor() as cursor:
            delete_script = 'DELETE FROM bank_account WHERE account_id = %s AND username = %s RETURNING account_id;'
            cursor.execute(delete_script, (account_id, username))
            deleted_id = cursor.fetchone()
            connection.commit()
            logging.info("Bank account deleted successfully!")
            return deleted_id
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error deleting bank account: {error}")
        connection.rollback()
        raise error

def delete_transaction(connection, username, transaction_id):
    try:
        with connection.cursor() as cursor:
            delete_script = 'DELETE FROM Transactions WHERE transaction_id = %s AND username = %s RETURNING transaction_id;'
            cursor.execute(delete_script, (transaction_id, username))
            deleted_id = cursor.fetchone()
            connection.commit()
            logging.info("Transaction deleted successfully!")
            return deleted_id
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error deleting transaction: {error}")
        connection.rollback()
        raise error

def delete_expense_category(connection, username, category_id):
    try:
        with connection.cursor() as cursor:
            delete_script = 'DELETE FROM expense_categories WHERE category_id = %s AND username = %s RETURNING category_id;'
            cursor.execute(delete_script, (category_id, username))
            deleted_id = cursor.fetchone()
            connection.commit()
            logging.info("Expense category deleted successfully!")
            return deleted_id
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error deleting expense category: {error}")
        connection.rollback()
        raise error

def delete_monthly_expense(connection, username, expense_id):
    try:
        with connection.cursor() as cursor:
            delete_script = 'DELETE FROM monthly_expenses WHERE expense_id = %s AND username = %s RETURNING expense_id;'
            cursor.execute(delete_script, (expense_id, username))
            deleted_id = cursor.fetchone()
            connection.commit()
            logging.info("Monthly expense deleted successfully!")
            return deleted_id
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error deleting monthly expense: {error}")
        connection.rollback()
        raise error


def get_user_info(connection, username_to_find):
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(query, (username_to_find,))
            user_information = cursor.fetchone()
            
            logging.info(f"{username_to_find} information fetched succefully!")
            return user_information
        
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error finding the user {username_to_find}: {error}")
        connection.rollback()
        raise error 


def add_user(connection, username, first_name, last_name, hashed_password):
    try:
        with connection.cursor() as cursor:
            insert_script = '''
                INSERT INTO bank_account (username, first_name, last_name, password_hash)
                VALUES (%s, %s, %s, %s)
                RETURNING *;
            '''
            cursor.execute(insert_script, (username, first_name, last_name, hashed_password))
            new_user = cursor.fetchone()
            connection.commit()
            logging.info("Bank account added successfully!")
            return new_user
    except Exception as error:
        logging.error(f"can't sign you up, the error is: {error}")
        connection.rollback()
        raise error
    return None
    
    
if __name__ == "__main__":
    connection = None
    try:
        connection = connect()
        if connection:
            user_info = (get_user_info(connection, "jdoe"))
    except Exception as error:
        logging.error(error)
    finally:
        if connection:
            connection.close()
            