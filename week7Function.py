"""
Function used for making dictionary with course prefix keys and tupple values of course numbers
"""
myTuple=input ('Please enter Course Prefix: ')
firstList = sorted(myTuple)
myDictionary = dict()

myDictionary[myTuple] = firstList


def printCourseDictionaryTuples(dictParm):
    print(type(dictParm))
    for key in myDictionary.keys():
        print(key)
    for item in myDictionary[key]:
        print(item)
