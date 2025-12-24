## Installation

 1. **Install PostgreSQL server and client**
<br>
`sudo dnf install postgresql-server postgresql-contrib`

2. **Initialize the database cluster**  
    This is required once after installation.<br>
`sudo postgresql-setup --initdb`

3. **Enable and start PostgreSQL**<br>
`sudo systemctl enable postgresql sudo systemctl start postgresql`

4. **Verify it’s running**<br>
`systemctl status postgresql`
5. **Accessing PostgreSQL**<br>
PostgreSQL creates a default Linux user called postgres. To manage the database, you need to execute commands as that user.
The quick way to enter the SQL shell:<br>

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

<br>
 Otherwise you can just:
`psql -d your_database_name -c "\dt"`
you can execute whatever command you want without having to login 

# The Command to run a file
To run the SQL file you are currently working on in SQLTools, use this command structure:
`psql -h <host> -U <username> -d <database> -f <filename.sql>`

- h: Host (e.g., localhost)
- U: Username (e.g., postgres)
- d: Database name
- f: The path to your SQL file

---
# Better practices:
1. Make a env file containing a bash script that loads your database's information. Like the following:
```sh
export PGHOST="localhost"
export PGPORT="5432"
export PGDATABASE="incomeDB"
export PGUSER="hajora"
export PGPASSWORD="*****"

echo "Database environment variables set for incomeDB." 
```
for this case run: 
`source db_env.sh` or `. db_env.sh`

2. Run your SQL file with only specify one thing: the file name.<br>
`psql -f filename.sql`

3. If you are joining two table, any column in the top SELECT line that is not inside the math parentheses MUST go in the GROUP BY line.


---

# DATE/Time

- this article is very interesting concerning the dates manipulation:<br>
https://www.geeksforgeeks.org/postgresql/postgresql-date-data-type/
<br>
- `SELECT EXTRACT (DAY / MONTH / YEAR from NOW());` : to get the current date information
---
# Code checking:
If your worry is that the script inserts data or deletes things, and you just want to check if the syntax (grammar) is correct without actually changing your database, wrap the code in a transaction with a rollback.<br>
Add BEGIN; at the very top and ROLLBACK; at the very bottom.

```sql
BEGIN; -- Start a transaction

-- Your crazy code here
INSERT INTO users (name) VALUES ('Test');
DELETE FROM orders WHERE id = 5;

ROLLBACK; -- Undo EVERYTHING that just happened```
```

---

# points to check:

1. Persistence: How to save code so it is not lost after the session ends (using SQL script files).
2. Versioning: How to manage changes (like adding a new table) after the database already contains data, without deleting that data (using incremental Migrations).
3. Synchronization: How the database knows which files it has already run so it doesn't try to create the same table twice (using a schema_migrations metadata table).

---
# Untrusted data
1. Indexation: it makes the search algorithm go from O(n) to O(1)
2. Hashing: hashmaps

--- 
- know the difference between LDD/LMD/LSD:
1. LDD: create, alter, drop
2. LMD: insert, update, delete, select
3. LSD: donner des privileges a des utilisateurs  (grant, deny, remove..)
