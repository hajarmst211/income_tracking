
# Income Tracker (PostgreSQL Learning Project)

This project is a simple command-line application built to practice **PostgreSQL** and **Python database interactions** using `psycopg2`. It models a basic personal income and expense tracking system.


## Project Goals
* Record incoming and outgoing transactions
* Categorize expenses to see what they spend money on every month
* Get a clearer picture of cash flow and spending habits
* Organize and priorities their monthly expenses

## Project Overview:

![Demo Screenshot](demonstation/demo1.png)


## Database Schema

The database tracks bank accounts, transactions, expense categories, and monthly expenses.<br>



## Project Structure

```
income_tracker/
│
├── config/
│   ├── database.ini          # Database credentials
│   └── settings.py           # ConfigParser logic to load the .ini
│
├── sql/                      # Raw SQL files for reference/setup
│   ├── 01_create_tables.sql
│   └── 02_insert_data.sql
│
├── src/
│   ├── __init__.py
│   ├── database/             # Database communication layer
│   │   ├── __init__.py
│   │   ├── connection.py     # Connection logic (Context Managers)
│   │   └── repository.py     # Pure SQL execution (add/delete/fetch)
│   │
│   ├── services/             # Business logic (Validation, Auth, Calculations)
│   │   ├── __init__.py
│   │   ├── auth_service.py   # Login/Sign-up logic (Hashing)
│   │   └── session.py        # Store the current logged-in user
│   │
│   └── ui/                   # User Interface (CLI)
│       ├── __init__.py
│       ├── menus.py          # Printing menus and getting choices
│       └── handlers.py       # Functions that bridge UI input to Services/DB
│
├── main.py                   # Application Entry Point
├── requirements.txt          # Dependencies
└── .gitignore                # Exclude __pycache__, .ini, etc.
```

---

## Setup Instructions

### 1. Create the Database

```sql
CREATE DATABASE incomeDB;
```

### 2. Configure Database Connection

Edit `database.ini`:

```ini
[postgresql]
host=localhost
database=incomeDB
user=your_user
password=your_password
port=5432
```

---

## Running the Application

From the `src` directory:

```bash
python main.py
```

You will interact with a CLI menu that allows you to:

* Add records
* Delete records
* Display tables

---

## Features

* Add bank accounts
* Record transactions
* Define expense categories
* Track fixed monthly expenses
* Delete records by ID
* Display database tables in terminal

---

## Future Improvements (Optional)

* Update operations
* Replace manual CLI inputs with interactive forms and buttons
* Better input validation
* Logging to file
* Docker setup

---

## License
1. Indeed, the Readme is AI made (under sever instructions) but the code is human written.<br>
2. This project is for learning purposes only.

