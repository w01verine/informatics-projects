#Dictionaries

#literal dictionary

myd = {"First Name":"Gerald","Last Name":"Emerick","Email":"jerryemerick@ferris.edu"}
print(myd["First Name"])

mylist = ["orange","mango"]
print (mylist[0])

#change dictionary value
myd["First Name"] = "Jerry"
print(myd["First Name"])
print(myd)

#add dictionary item
myd["Office"] = "IRC 212B"
print(myd)

keyList = myd.keys()
print(keyList)

#values
valuesList = myd.values()
print(valuesList)


if "Office" in keyList:
    print("office found")
else:
    print("office not found")

mystring = "Jerry"
if "e" in mystring:
    print("letter e found in string")

if "Jerry" in valuesList:
    print("Jerry found")
else:
    print("Jerry not found")

#iterate / loop through list of values

for item in keyList:
    (print(item))
    if item == "office":
         print(sorted(keyList))
#sorting
   

mylist = ["orange","pear"]
myd = {"First Name":"Gerald","Last Name":"Emerick","Email":"jerryemerick@ferris.edu"}

#list constructor
mylist = list()
"can put a string in here or not"
mystring=""

#dictionary constructor
myd = dict()

mylist.append("orange")
mylist.append("apple")

mykey = input("Please enter a key: ")

myd[mykey] = myvalue

print(myd)

#myd["First Name"] = "Jerry"