"""
Function used for making dictionary with course prefix keys and tupple values of course numbers
"""
myISINtuple = ("", "200", "499","234")
myISINlist = sorted(myISINtuple)
myISYStuple = ("320","240","225","410")
myISYSlist = sorted(myISYStuple)

myDictionary = dict()

myDictionary["octet"] = myISINlist

def countIPAddress(listParm):
    print(type(listParm))
    for key in myDictionary.keys():
        print(key)
    for item in myDictionary[key]:
        print(item)
  
