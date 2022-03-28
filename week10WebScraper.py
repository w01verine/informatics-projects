"""
Writes List of urls to file
"""
#http get a file and save in python string variable
#check http  code
from bs4 import BeautifulSoup

import urllib.request, urllib.parse, urllib.error
import re

import urllib.request
fhand = urllib.request.urlopen('http://ec2-100-25-160-206.compute-1.amazonaws.com/') 
for line in fhand:
    print(line.decode().strip())


resp = urllib.request.urlopen("http://ec2-100-25-160-206.compute-1.amazonaws.com/")
soup = BeautifulSoup(resp,"html.parser")
tags = soup('a')
print(type(tags))
for tag in tags:
    print (tag.get('href',None))



'''
        #print(resp.headers('href'))
#for tag in tags:
#    print (tag.string)
#    print(str(tag))
    #search for text in the tag
 #   if "logo" in str(tag).lower():
#        print (tag)
 #   print(tag.contents[0])

#save downloaded file to disk
try:
    resp = urllib.request.urlopen('http://ec2-100-25-160-206.compute-1.amazonaws.com/')
    bytesToWrite = resp.read()
    
    #must write as binary to maintain unicode formatting
    myFile = open("ferrislinks.txt",'wb')
    myFile.write(bytesToWrite)
    myFile.close()
    
except Exception as exc:
    print('An error occured.' + str(exc))
'''








#converts the response object data into a BeautifulSoup object
soup = BeautifulSoup(resp,"html.parser")
#get a list of anchor <a> tags
tags = soup('a')
print(type(tags))
for tag in tags:
    print (tag.get('href',None))
    #search for text in the tag
    if "ukraine" in str(tag).lower():
        print("Word 'ukraine' found in " + str(tag.get("href",None)))
#implement exception handling
#change the name of the file or URL to cause an HTTP error
try:
    resp = urllib.request.urlopen("https://www.cnn.com")
except Exception as exc:
    print('An error occured.' + str(exc))

#save downloaded file to disk
try:
    resp = urllib.request.urlopen('http://ec2-100-25-160-206.compute-1.amazonaws.com/')
    bytesToWrite = resp.read()
    
    #must write as binary to maintain unicode formatting
    myFile = open("ferrislinks.txt",'wb')
    myFile.write(bytesToWrite)
    myFile.close()
    
except Exception as exc:
    print('An error occured.' + str(exc))