


word = input()
password = ''
i = 0
while i < len(word):
    ch = word[i]
    if ch == 'i':
        password += '1'
    elif ch == 'a':
        password += '@'
    elif ch == 'm':
        password += 'M'
    elif ch == 'B':
        password += '8'
    elif ch == 's':
        password += '$'
    else:
        password += ch
    i += 1
password += "!"
print(password)