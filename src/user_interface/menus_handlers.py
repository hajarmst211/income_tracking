# menus_handles.py

from src.services.auth_services import is_password_correct
from src.user_interface.db_operations_handlers import *
from src.user_interface.menus import welcome_menu, main_menu, addition_menu, login_menu, suppression_menu, table_display_menu
import logging
import sys

def welcome_handler(connection, active_session):
    try:
        choice = welcome_menu()
        match choice:
            case 1:
                handle_login(connection, active_session)
            case 2: 
                create_user_cli(connection)
                handle_login(connection, active_session)
            case 3:
                return 0
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
        sys.exit(130)
        return 1


def handle_main_menu(connection, active_session):
    try:
        current_user = active_session.current_user
        choice = main_menu(current_user)
        match choice:
            case 1:
                handle_addition(connection, current_user)
            case 2:
                handle_deletion(connection, current_user)
            case 3:
                handle_display(connection, current_user)
            case 4:
                active_session.close_session()
                return 0
                
    except (Exception, KeyboardInterrupt)as error:
        logging.error(error)
    return 0
    
  
def handle_login(connection, active_session):
    username, input_password = login_menu()
    password_bytes = input_password
    #.encode('utf-8')
    
    authenticated = is_password_correct(connection, username, password_bytes)
    if authenticated:
        active_session.current_user = username
        handle_main_menu(connection, active_session)
        return 0 
    else:
        logging.error('''
                      Something is wrong in your authentication, try again!\n 
                      If you don't have an account feel free to sign in.\n
                      ''')
    return 1
  
def handle_addition(connection, current_user):
    try:
        choice = addition_menu(current_user)
        match choice:
            case 1:
                create_bank_account(connection, current_user)
            case 2: 
                create_transaction(connection, current_user)
            case 3:
                create_expense_category(connection, current_user)
            case 4:
                create_monthly_expense(connection, current_user)
            case 5:
                handle_main_menu(connection, current_user)
                return 
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
        return 1
     

def handle_deletion(connection, current_user):
    try:
        choice = suppression_menu()
        match choice:
            case 1:
                delete_bank_account(connection, current_user)
            case 2: 
                delete_transaction(connection, current_user)
            case 3:
                delete_expense_category(connection, current_user)
            case 4:
                delete_monthly_expense(connection, current_user)
            case 5:
                handle_main_menu(connection, current_user)
                return 
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
        return 1
    
    
def handle_display(connection, current_user):
    try:
        choice = table_display_menu()
        match choice:
            case 1:
                display_table(connection, 'bank_account', current_user)
            case 2: 
                display_table(connection,'Transactions', current_user)
            case 3:
                display_table(connection,'expense_categories', current_user)
            case 4:
                display_table(connection,'monthly_expenses', current_user)
            case 5:
                handle_main_menu(connection, current_user)
                return 
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
        return 1
    