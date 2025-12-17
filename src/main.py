from cli import *

#local functions:
from connection import connect
from db_operations import display_table


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
            
            
def display_table_choice(table_name, connection):
    match table_name:
        case 1:
            table_name = "bank_account"
            display_table(connection, table_name)
        case 2:
            table_name = "Transactions"
            display_table(connection, table_name)
        case 3:                
            table_name = "expense_categories"
            display_table(connection, table_name)
        case 4:
            table_name = "monthly_expenses"
            display_table(connection, table_name)
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
                table_choice = table_display_menu()
                display_table_choice(connection, table_choice)
                
            case 4:
                break
    if connection:
        connection.close()
    
    
if __name__ == "__main__":
    main()