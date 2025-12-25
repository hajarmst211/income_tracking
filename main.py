# main.py

#local functions:
from src.user_interface.menus_handlers import welcome_handler, handle_login
from src.database.connection import connect   
from src.services.session import active_session
from src.services.auth_services import debug_is_password_correct
#src/services/session.py
import sys

def main():
    try:
        connection = connect()
        
        while 1:
            welcome_handler(connection, active_session)
            
    except Exception as error:
        raise error
    
    if connection:
        connection.close()
    
    return 0
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
            print("Programme interrupted by the user")
            sys.exit(130)
    