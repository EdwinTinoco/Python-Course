import bcrypt
import sqlite3

conn = sqlite3.connect("employees.db")
print("Opened DB connection")

data = conn.execute("SELECT id, username, password, age FROM EMPLOYEES")

for row in data:
    print("ID = ", row[0])
    print("USERNAME = ", row[1])
    print("HASHED_PW = ", row[2])
    print("AGE = ", row[3], "\n")

    password_hash = row[2]
    user_password = input("Please verify passwrod: ")

    valid_password = bcrypt.hashpw(user_password.encode(), password_hash) == password_hash

    if valid_password:
        print("Password is a match!\n")
    else:
        print("Invalida credentials\n")


print("Data returns successfully")

conn.close()
print("connection close")



