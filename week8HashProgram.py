"""
Week 8 Hash Program
"""
import hashlib
import week8HashFunctions
import validatepswd1

pswd = input("Please enter your password: ")
#encode the string (required by hashlib)
pswd = pswd.encode("utf-8") #utf 16 for multilanguages

myHash = hashlib.md5(pswd)

#get hashvalue
myhashvalue = myHash.hexdigest()
print(validatepswd1.validatePassword(pswd))
