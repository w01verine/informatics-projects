import urllib.request
import json

webres = urllib.request.urlopen("https://cve.circl.lu/api/last")

cvedata = webres.read()
#    print(type(cvedata))

#decode bytes as utf8
jscvedata = json.loads(str(cvedata.decode('utf-8')))


print(type(jscvedata))

#list of result dictionaries
#interate each dictionary of results in the list
for dictItem in jscvedata:
    print (dictItem["summary"] + "\n\n")

'''
#menu
#change the code above to a function
#get the input from user - menu option and the search term


#menu

while True:
    print("option 1")
    print ("option 2")
    userValue = input("select an option")
    
    #evaluate userValue, call function with input
'''