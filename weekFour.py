#iteration / While loops

#prompt user for a strring and prin the string
#quit program when user types "quit"
'''
while True: #infinate
    #while loop body
    userWord = input("Please enter a word: ")
    if userWord != "quit":
        print(userWord)
    else:
        break #stop the while

print("program has ended.")
'''
#while loop with a cconditional expression

#Get input
sentence = ""
counter = 0
counter = int(counter) + 1
answer = ""
userWord = ""


while (answer!="yes" and answer!="no"):
    answer = input("Would you like to enter another line? Please, type yes or no: ").lower()

    if answer.lower() == "no":
        break
    else:
        sentence = "Line " + str(counter) + sentence + userWord + "\n"
        
while (userWord != "no") :
    userWord = input("Type your next line here: ")
    if userWord != "no":
        print(userWord)

sentence = sentence.lower()


print(sentence) 

print("program has ended.")
