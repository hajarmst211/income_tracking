from cli import *

from connection import connect

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
            delete_bank_account(connection)
        case 2:
            delete_transaction(connection)
        case 3:                
            delete_expense_category(connection)
        case 4:
            delete_monthly_expense(connection)
        case 5:
            main_menu()
            


def main():
    connection = connect()
    while(1):
        choice = main_menu()
        match choice:
            case 1:
                addition_choice = addition_menu()
                addition_cases(addition_choice, connection)
            case 2:
                suppression_choice = suppression_menu()
                suppression_cases(suppression_choice, connection)
            case 3:
                break
    
    
if __name__ == "__main__":
    main()