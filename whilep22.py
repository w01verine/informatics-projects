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
'''
#while loop with a cconditional expression
userWord = ""
counter = 0 #count and control the number of iterations. Max 5

while (userWord != "quit") and (counter < 5):
    userWord = input("Please enter a word: ")
    if userWord != "quit":
        print(userWord)
    '''
#Get input
sentence = ""
counter = 0
counter = counter + 1
userWord = float(userWord)
while (answer!="yes" and answer!="no"):
    answer = input("Would you like to enter another line? Please, type yes or no: ").lower()

def getUserInput():
    while True:
    userWord = input("Type your next line here: ")
    if userWord.lower() == "yes":
        break
    else:
    sentence = "Line " + str(counter) + sentence + userWord + "\n"
    

sentence = sentence.lower()


print(sentence) 

print("program has ended.")



sentence = ""
counter = 0
while True:
    userWord + input("Please a word for your sentence or enter 'quit': ")
    if userWord.lower() == "quit":
        break
    else:
        sentence = "Line " + str(counter) + sentence + userWord + "\n"

print(sentence)
sentence = sentance.lower()
print(sentence)
