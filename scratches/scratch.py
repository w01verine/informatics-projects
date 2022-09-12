"""
Your module description
"""

import sqlite3, sqlite3.connect, os, sys
import hashlib


conn = sqlite3.connect('userdb.sqlite3')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Users')
cur.execute('CREATE TABLE USERS(username TEXT, password TEXT)')

#cur = conn.cursor()


#cur.execurte("INSERT INTO uSERS (username, password) VALUES ('student1', '460899c942673a93b86a81ca0297cd36')")

cur.execurte('INSERT INTO uSERS (username, password) VALUES (?,?)', ('student1', '460899c942673a93b86a81ca0297cd36'))

conn.commit()


while 1==1:
    #TODO #1 prompt use the user for a user name and pasword.
    #store the entered username in a variable named "uname"
    #store the entered password in a variable named "pswd"
    uname = "student1"
    cur.execute("SELECT password from users WHERE username = ?", (uname,))
    row=cur.fetchone()
    break

    if row == None:
        print("User name is incorrect. Try again...")

    else:
    #TO DO #3, row variable is a tuple. Compare the first elemen in the row tuple to your hashed password pswdHash
    #display appropriate

conn.close()