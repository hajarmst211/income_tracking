# menus_handles.py

import menus
from services. auth_services import is_password_correct
from db_operations_handlers import *
import logging


def welcome_handler(choice):
    try:
        match choice:
            case 1:
                menus.login_menu()
            case 2: 
                signup_menu()
            case 3:
                return 0
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
        return 1


def handle_login(username, hashed_password):
    authenticated = is_password_correct(username, hashed_password)
    if authenticated:
        menus.main_menu()
    else:
        logging.error('''
                      Something is wrong in your authentication, try again!\n 
                      If you don't have an account feel free to sign in.\n
                      ''')
        menus.welcome_menu()
    return


def handle_signup():
    user_creation_output = create_user_cli()
    if user_creation_output == 0:
        handle_login()
    else:
        signup_menu()
    return 
        
    
def handle_addition(connection, current_user):
    try:
        choice = menus.addition_menu()
        match choice:
            case 1:
                create_bank_account(connection)
            case 2: 
                create_transaction(connection)
            case 3:
                create_expense_category(connection)
            case 4:
                create_monthly_expense(connection)
            case 5:
                menus.main_menu()
                return 
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
        return 1
    

def handle_deletion(connection, current_user):
    try:
        choice = menus.suppression_menu()
        match choice:
            case 1:
                delete_bank_account(connection)
            case 2: 
                delete_transaction(connection)
            case 3:
                delete_expense_category(connection)
            case 4:
                delete_monthly_expense(connection)
            case 5:
                menus.main_menu()
                return 
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
        return 1
    
    
def handle_display(connection, current_user):
    try:
        choice = menus.table_display_menu()
        match choice:
            case 1:
                display_table(connection, 'bank_account')
            case 2: 
                display_table(connection,'Transactions')
            case 3:
                display_table(connection,'expense_categories')
            case 4:
                display_table(connection,'monthly_expenses')
            case 5:
                menus.main_menu()
                return 
    except KeyboardInterrupt:
        print("Operations cancelled by the user!")
        return 1