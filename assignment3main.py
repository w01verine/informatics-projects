import assignment3functions


myGPA = input("Please Enter Your GPA: ")
#pass the input to the displayGrade function 
outputValue = int("myGPA")
if myGPA >=3.5:
    print("You received an A")
elif myGPA >=3.0 and myGPA < 3.5:
    print("You received a B")
elif myGPA >=2.0 and myGPA < 3.0:
    print("You received a C")
elif myGPA < 2.0:
    print("You should consider retaking the course")
        
