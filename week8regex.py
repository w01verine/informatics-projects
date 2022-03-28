"""
Your module description
"""
pswd = input("Please enter your password: ")
import re
def passwordValidate(s):
    if re.search("[0-9]", s[0]):
        return False
    elif 'qwerty' in s or '1234'in s:
        return False
    elif len(s)<10:
        return False
    elif not re.search("[A-Z]", s):
        return False
    elif not re.search("[0-9]", s):
        return False
    elif not re.search("[!@#$%^&*()=+]", s):
        return False
    else:
        return True
if passwordValidate()