# auth_services.py

import logging
from werkzeug.security import check_password_hash


def is_password_correct(user_information, input_password):
    try:
        if user_information is None:
            logging.error("User not found in database")
            return False
        
        db_password = user_information[3]
        is_correct = check_password_hash(db_password, input_password)
        return is_correct

    except Exception as error:
        logging.error(f"The error that occurred isc:{error}")
    
