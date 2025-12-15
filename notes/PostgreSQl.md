## Installation

 1. **Install PostgreSQL server and client**
`sudo dnf install postgresql-server postgresql-contrib`

2. **Initialize the database cluster**  
    This is required once after installation.
`sudo postgresql-setup --initdb`

3. **Enable and start PostgreSQL**
`sudo systemctl enable postgresql sudo systemctl start postgresql`

4. **Verify it’s running**
`systemctl status postgresql`
5. **Accessing PostgreSQL**
PostgreSQL creates a default Linux user called postgres. To manage the database, you need to execute commands as that user.
The quick way to enter the SQL shell:

`sudo -u postgres psql`

Type \q and hit Enter to exit back to your normal terminal.

---
# Create users and databases:
1. Switch to the postgres user:
`sudo -i -u postgres`

2. Create a new database user (Role):
It is best practice to create a database user that matches your Linux username. This allows you to log in easily later without password prompts (using "peer authentication").

`createuser --interactive`

Enter name of role: (Type your actual Fedora username, e.g., john)
Shall the new role be a superuser? Type y (since this is your computer and your development database).

3. Create a database:
Now create a database. Often, people create a database with the same name as their user, or a specific project name.

`createdb my_first_db`

4. Exit the postgres user:
Type exit to go back to your normal user.

# Enter the SQL Shell (psql)
Now that you have created a user that matches your Linux login (in step A.2), you can access the database directly from your normal terminal:

`psql -d my_first_db`

- To list databases: \l
- To list tables: \dt
- To quit: \q

# The Command to run a file
To run the SQL file you are currently working on in SQLTools, use this command structure:
`psql -h <host> -U <username> -d <database> -f <filename.sql>`

- h: Host (e.g., localhost)
- U: Username (e.g., postgres)
- d: Database name
- f: The path to your SQL file
---

# points to check:

1. Persistence: How to save code so it is not lost after the session ends (using SQL script files).
2. Versioning: How to manage changes (like adding a new table) after the database already contains data, without deleting that data (using incremental Migrations).
3. Synchronization: How the database knows which files it has already run so it doesn't try to create the same table twice (using a schema_migrations metadata table).
