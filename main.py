from database.user_interface.menus import *

#local functions:
from database.connection import connect
from database.repository import display_table


def addition_cases(addition_choice, connection):
    match addition_choice:
        case 1:
            create_bank_account(connection)
        case 2:
            create_transaction(connection)
        case 3:                
            create_expense_category(connection)
        case 4:
            create_monthly_expense(connection)
        case 5:
            main_menu()
            

def suppression_cases(suppression_choice, connection):
    match suppression_choice:
        case 1:
            delete_bank_account_cli(connection)
        case 2:
            delete_transaction_cli(connection)
        case 3:                
            delete_expense_category_cli(connection)
        case 4:
            delete_monthly_expense_cli(connection)
        case 5:
            main_menu()
            
            
def display_table_choice(connection, table_choice):
    match table_choice:
        case 1:
            display_table(connection, 'bank_account')
        case 2:
            display_table(connection, 'Transactions')
        case 3:
            display_table(connection, 'expense_categories')
        case 4:
            display_table(connection, 'monthly_expenses')
        case 5:
            main_menu()

def main():
    while(1):
        connection = connect()
        choice = main_menu()
        match choice:
            case 1:
                addition_choice = addition_menu()
                addition_cases(addition_choice, connection)
                
            case 2:
                suppression_choice = suppression_menu()
                suppression_cases(suppression_choice, connection)
                
            case 3: 
                table_choice = table_display_menu()
                display_table_choice(connection, table_choice)
                
            case 4:
                break
    if connection:
        connection.close()
    
    
if __name__ == "__main__":
    main()