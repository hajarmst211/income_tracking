# main.py

#local functions:
from src.user_interface.menus import *
from src.user_interface.menus_handlers import *
from src.database.connection import connect   
from src.services.session import active_session

def main():
    try:
        connection = connect()
        
        while active_session.username is None:
            choice = welcome_menu()
            match choice:
                case 1:
                    login_menu(connection, active_session)
                        
                case 2:
                    signup_menu(connection)
                        
                case 3: 
                    return
        
        while True:
            current_user = active_session.current_user()
            choice = main_menu()
            
            if choice == 1:
                handle_addition(connection, current_user)
            elif choice == 2:
                handle_deletion(connection, current_user)
            elif choice == 3:
                handle_display(connection, current_user)
            elif choice == 4:
                print("Goodbye!")
                break
            
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
     
    if connection:
        connection.close()
    
    return 0
    
if __name__ == "__main__":
    main()