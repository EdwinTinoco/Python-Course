import sqlite3

conn = sqlite3.connect("employees.db")
print("Opened DB connection")

user_id = input("Enter an ID to delete: ")

conn.execute(f"DELETE FROM EMPLOYEES where ID = {user_id}")
conn.commit()

print("Data deletion successful")

conn.close()
print("connection close")
