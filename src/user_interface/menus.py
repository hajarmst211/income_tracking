#menus.py

#standard function:
from decimal import Decimal
from menus_handlers import welcome_menu_handler
import logging

def welcome_menu():
    choice_script = '''
                    Hi, welcome to your income tracking interface.
                    login or sign in:
                    [1] login
                    [2] sign in
                    [3] quit
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1,4):
            logging.error("The choice is out of range, it must be between 1 to 3")
    except ValueError :
        logging.error("Invalid value! Give an integer")
    
    welcome_menu_handler(choice)  
    return 0

def login_menu():
    username= input("Enter your username:\n")
    password= input("Entre the password:\n")

def sign_in_menu():
    print("new_user") 

def main_menu():
    choice_script = '''
                    Hi, welcome to your income tracking interface.
                    What type of transaction you want to make:
                    [1] Add a row
                    [2] Delete a row
                    [3] Display a table
                    [4] quit
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1,5):
            logging.error("The choice is out of range, it must be between 1 to 4")
    except ValueError :
        logging.error("Invalid value! Give an integer")
        
    return choice

def addition_menu():
    choice_script = '''
                    Hi,
                    What type of addition you want to do:
                    [1] Add Bank Account
                    [2] Add Transaction
                    [3] Add Expense Category
                    [4] Add monthly expense
                    [5] Back to main menu
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1,6):
            logging.error("The choice is out of range, it must be between 1 to 5")
    except ValueError :
        logging.error("Invalid value! Give an integer")
        
    return choice


def suppression_menu():
    choice_script = '''
                    Hi,
                    What type of suppression you want to do:
                    [1] delete Bank Account
                    [2] delete Transaction
                    [3] delete Expense Category
                    [4] delete monthly expense
                    [5] Back to main menu
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1,6):
            logging.error("The choice is out of range, it must be between 1 to 5")
    except ValueError :
        logging.error("Invalid value! Give an integer")
        
    return choice


def table_display_menu():
    choice_script = '''
                    Hi,
                    What table you want to display:
                    [1] Bank Account
                    [2] Transaction
                    [3] Expense Category
                    [4] monthly expense
                    [5] Back to main menu
                    '''
    try:                
        choice = int(input(choice_script))
        if choice not in range(1,6):
            logging.error("The choice is out of range, it must be between 1 to 5")
    except ValueError :
        logging.error("Invalid value! Give an integer")
        
    return choice