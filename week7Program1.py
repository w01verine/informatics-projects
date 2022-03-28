import week7Function

myDictionary = dict()
while True:
    coursePrefix = input("Please enter your course prefix or type 'quit': ")
    #quit
    if coursePrefix.lower() == 'quit':
        break
    else:
        while True:
            courseNumbers = input("Please enter your course number or type 'done': ")
            if courseNumbers.lower() == 'done':
                week7Function.printCourseDictionaryTuples(myDictionary)
    
            