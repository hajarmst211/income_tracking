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
            print("Please log in first.")
            handle_login(conn)
        
        
        choice = welcome_menu()
        match choice:
            case 1:
                current_user = login_menu(connection)
                    
            case 2:
                sign_in_menu(connection)
                    
            case 3: 
                return
        
        while True:
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