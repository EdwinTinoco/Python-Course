import sqlite3

conn = sqlite3.connect('employees.db')

print("Database connection is sucessful.")

conn.execute("""
            CREATE TABLE EMPLOYEES
            (
                ID INTEGER PRIMARY KEY NOT NULL,
                USERNAME TEXT NOT NULL,
                PASSWORD TEXT NOT NULL,
                AGE INT NOT NULL
            );
            """)

print("Table created successfully")