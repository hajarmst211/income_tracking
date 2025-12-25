# auth_services.py

import logging
from werkzeug.security import check_password_hash
from src.database.repository import get_user_info
import bcrypt

def is_password_correct(connection, username, input_password):
    try:
        user_information = get_user_info(connection, username)
        if user_information is None:
            logging.error("User not found in database")
            return False
        
        db_password = user_information[3]
        is_correct = bcrypt.checkpw(
            input_password.encode('utf-8'), 
            db_password.encode('utf-8')
        )
        return is_correct

    except Exception as error:
        logging.error(f"The error that occurred isc:{error}")
    
    
def debug_is_password_correct(connection, username, input_password):
    try:
        user_information = get_user_info(connection, username)
        print(f"DEBUG 1: this is the user information fetched:{user_information}")
        if user_information is None:
            logging.error("User not found in database")
            return False
        
        db_password = user_information[3]
        print(f"DEBUG 2: this is the password fetched from the database:{db_password}")        
        is_correct = bcrypt.checkpw(
            input_password.encode('utf-8'), 
            db_password.encode('utf-8')
        )
        print(f"DEBUG 3: this is the is_correct variable value:{is_correct}")
        return is_correct

    except Exception as error:
        logging.error(f"The error that occurred isc:{error}")
    
