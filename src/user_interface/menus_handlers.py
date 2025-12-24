# menus_handles.py

from menus import welcome_menu, main_menu, login_menu, sign_in_menu
from src.services. auth_services import is_authentication_valid
import logging


def welcome_menu_handler(choice):
    try:
        match choice:
            case 1:
                login_menu()
            case 2: 
                sign_in_menu()
            case 3:
                return 0
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
        return 1


def logging_menu_handler(username, hashed_password):
    authenticated = is_authentication_valid(username, hashed_password)
    if authenticated:
        main_menu()
    else:
        logging.error('''
                      Something is wrong in your authentication, try again!\n 
                      If you don't have an account feel free to sign in.\n
                      ''')
        welcome_menu()
    return


 
