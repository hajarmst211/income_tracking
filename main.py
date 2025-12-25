# main.py

#local functions:
from src.user_interface.menus_handlers import welcome_handler
from src.database.connection import connect   
from src.services.session import active_session

import sys

def main():
    try:
        connection = connect()
        
        while True:
            welcome_handler(connection, active_session)
            current_user = active_session.current_user()
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
    