# main.py

#local functions:
from src.user_interface.menus import *
from src.user_interface.menus_handlers import *
from src.database.connection import connect   

def main():
    connection = connect()
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
     
    if connection:
        connection.close()
    
    
if __name__ == "__main__":
    main()