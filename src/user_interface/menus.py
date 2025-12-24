# menus.py

import logging
from menus_handlers import *

def welcome_menu(connection, active_session):
    choice_script = '''
                    Hi, welcome to your income tracking interface.
                    For the main menu make sure you login or sign in first:
                    [1] login
                    [2] sign up
                    [3] quit
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1, 4):
            logging.error("The choice is out of range, it must be between 1 to 3")
        return choice
        
        welcome_handler(connection, active_session, choice)
    except ValueError:
        logging.error("Invalid value! Give an integer")
        return welcome_menu(connection, active_session)
    return 0

def login_menu(connection, active_session):
    try:
        username = input("Enter your username:\n").strip()
        if not username:
            print("Error: Username cannot be empty.\n")
            return 1
        
        password = input("Enter the password:\n")
        if not password:
            print("Error: Password cannot be empty.\n")
            return 1

        password_bytes = password.encode('utf-8')
        success = handle_login(connection, active_session, username, password_bytes)
        return 0 if success else 1

    except UnicodeEncodeError:
        print("Error: Password contains invalid characters.\n")
        return 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1

def signup_menu(connection):
    try:
        handle_signup(connection)
        logging.info("Account created successfully!\n")
        return 0
    except UnicodeEncodeError:
        print("Error: Input contains invalid characters.\n")
        return 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1

def main_menu(username):
    choice_script = f'''
                    Logged in as: {username}
                    What type of transaction you want to make:
                    [1] Add a row
                    [2] Delete a row
                    [3] Display a table
                    [4] Logout/Quit
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1, 5):
            logging.error("The choice is out of range, it must be between 1 to 4")
            return main_menu(username)
        return choice
    except ValueError:
        logging.error("Invalid value! Give an integer")
        return main_menu(username)

def addition_menu(username):
    choice_script = f'''
                    Add entry for: {username}
                    What type of addition you want to do:
                    [1] Add Bank Account
                    [2] Add Transaction
                    [3] Add Expense Category
                    [4] Add monthly expense
                    [5] Back to main menu
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1, 6):
            logging.error("The choice is out of range, it must be between 1 to 5")
            return addition_menu(username)
        return choice
    except ValueError:
        logging.error("Invalid value! Give an integer")
        return addition_menu(username)

def suppression_menu(username):
    choice_script = f'''
                    Delete entry for: {username}
                    What type of suppression you want to do:
                    [1] delete Bank Account
                    [2] delete Transaction
                    [3] delete Expense Category
                    [4] delete monthly expense
                    [5] Back to main menu
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1, 6):
            logging.error("The choice is out of range, it must be between 1 to 5")
            return suppression_menu(username)
        return choice
    except ValueError:
        logging.error("Invalid value! Give an integer")
        return suppression_menu(username)

def table_display_menu(username):
    choice_script = f'''
                    Displaying data for: {username}
                    What table you want to display:
                    [1] Bank Account
                    [2] Transaction
                    [3] Expense Category
                    [4] monthly expense
                    [5] Back to main menu
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1, 6):
            logging.error("The choice is out of range, it must be between 1 to 5")
            return table_display_menu(username)
        return choice
    except ValueError:
        logging.error("Invalid value! Give an integer")
        return table_display_menu(username)