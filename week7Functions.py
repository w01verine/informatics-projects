"""
Function used for making dictionary with course prefix keys and tupple values of course numbers
"""
myISINtuple = ("300", "200", "499","234")
myISINlist = sorted(myISINtuple)
myISYStuple = ("320","240","225","410")
myISYSlist = sorted(myISYStuple)

myDictionary = dict()
myDictionary2 = dict()

myDictionary["ISIN"] = myISINlist
myDictionary2["ISYS"] = myISYSlist

def courseDictionary(dictParm):
    print(type(dictParm))
    for key in myDictionary.keys():
        print(key)
    for item in myDictionary[key]:
        print(item)
    for key in myDictionary2.keys():
        print(key)
    for item in myDictionary2[key]:
        print(item)
