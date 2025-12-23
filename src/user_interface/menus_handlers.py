# menus_handles.py

from menus import login_menu, sign_in_menu
from services. auth_services import is_authentication_valid
import logging


def welcome_menu_handler(choice):
    match choice:
        case 1:
            login_menu()
        case 2: 
            sign_in_menu()
        case 3:
            return 0

def logging_menu_handler(username, password):
    log_in = is_authentication_valid
    if log_in == False:
        logging.error("Authentication failed")
        login_menu()
    return 0


def 
