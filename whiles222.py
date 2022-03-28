
sentence = ""
counter = 0
counter = counter + 1
while True:
    userWord = input("Please a word for your sentence or enter 'quit': ")
    if userWord.lower() == "quit":
        break
    else:
        sentence = "Line " + str(counter) + sentence + userWord + "\n"
sentence = sentence.lower()
print(sentence)
