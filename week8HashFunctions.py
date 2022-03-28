"""
Week 8 Hash Functions
"""
import hashlib

def createRainbow():
    #open dictionary with "ISO-8859-1" encoding
    myList = open("english.txt","r", encoding="ISO-8859-1")
    #open output file for writing
    output = open("englishrainbow.txt","a")
    for line in myList:
        #convert to utf-8 encoding
        encoded_line = line.encode("utf-8")
        #create  md5 hash value of each word
        result = hashlib.md5(encoded_line)
        #convert hash value to string for writing to file
        md5Hash = str(result.digest())
        #write to output file "rainbow.txt"
        output.write(md5Hash + "\n")
# Calling the function
createRainbow()