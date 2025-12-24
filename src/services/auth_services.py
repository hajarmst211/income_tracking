# auth_services.py

import logging
from werkzeug.security import check_password_hash
from database.repository import get_user_info

def is_password_correct(connection, username, input_password):
    try:
        user_information = get_user_info(connection, username)
        if user_information is None:
            logging.error("User not found in database")
            return False
        
        db_password = user_information[3]
        is_correct = check_password_hash(db_password, input_password)
        return is_correct

    except Exception as error:
        logging.error(f"The error that occurred isc:{error}")
    
