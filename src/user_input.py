#user_input.py

import logging
import psycopg2

from  connection import connect 

def get_monthly_expenses(connection):
    try:
        expense_category = input("Provide an expense_category: \n")
        category_description = input("Provide a description: \n")
        with connection.cursor() as cursor:
            insert_script = '''
                                INSERT INTO expense_categories (name, description) 
                                VALUES (%s, %s)
                            ''' 
                        
            cursor.execute(insert_script, (expense_category, category_description))
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        raise error


if __name__ == "__main__":
    try:
        connection =  connect()
        if connection is not  None:
            get_monthly_expenses(connection)
            connection.commit()
            
        
    except Exception as error:
        logging.error(error)
        if connection:
            connection.rollback()
    
    finally:
        if connection:
            connection.close()
            
    