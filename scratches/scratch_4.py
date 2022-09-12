import sqlite3
import hashlib

# create database
conn = sqlite3.connect('userdb.sqlite3')

# instantia a cursor object
cur = conn.cursor()

# create table
cur.execute('DROP TABLE IF EXISTS Users')
cur.execute('CREATE TABLE Users(username TEXT, password TEXT)')
cur = conn.cursor()

# create a user record with unhashed password of "WeakPassword"
cur.execute('INSERT INTO Users (username, password) VALUES (?,?)', ('student1', '460899c942673a93b86a81ca6297cd36'))

cur.execute('INSERT INTO Users(username,password) VALUES("admin","8b1a9953c4611296a827abf8c47804d7")')

while 1 == 1:
    # TO DO #1 prompt use the user for a user name and password.

    # store the entered username in a varaible named "uname"
    uname = input("Enter your username: ")

    # store the entered password in a varaible named "pswd"
    pswd = input("Enter your password: ")

    # TO DO #2 hash the user provided password (pswd) as an md5 hash using hashlib and store in variable name              pswdHash
    pswdHash = hashlib.md5(pswd.encode())
    pswdHash.hexdigest()

    # fetch the hashed password from the database for the user uname (the following code is vulnerble to SQL Injection...)
    cur.execute("SELECT password from Users WHERE username = ?", (uname,))
    row = cur.fetchone()

    if row == None:
        print("user name is incorrect.  Try again...")

    else:
        if (row[0] == pswdHash.hexdigest()):

            print("Password is correct")
            break
        else:
            print("Password was incorrect")
            # TO DO #3.  row variable is a tuple.   Compare the first element in the row tuple to your hashed password pswdHash
            # display appropriate messages to user.   "break" if the hashed password are equal

# close database connection
conn.close()