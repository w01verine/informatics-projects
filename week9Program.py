"""
Your module description
"""
#function header
def printCourseDictionaryTuples (dictTupleInput):
    #for keys in dictTupleInput
    for k in dictTupleInput:
        #print key
        print(k)
        #sort the tuple
        dictTupleInput[k].sort()
        #print all values
        for v in dictTupleInput[k]:
            print(v)
if __name__ == '__main__':
    #declare empty dictionary
    Dictionary={}
    #get course prefix from user
    prefix=input("Enter a course prefix or 'quit': ")
    #untill prefix is not quit the loop executes
    while(prefix!="quit"):
        #declare empty list course_number
        course_number=[]
        #get courseno from user
        courseno=input("Enter a course number or 'done': ")
        while(courseno!="done"):
            course_number.append(courseno)
            courseno=input("Enter a course number or 'done': ")
        #set key and value as tuple
        Dictionary[prefix]=course_number
        prefix=input("Enter a course prefix or 'quit': ")
    #call function printCourseDictionaryTuples()
    printCourseDictionaryTuples(Dictionary)