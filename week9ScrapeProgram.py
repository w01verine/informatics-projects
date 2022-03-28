"""
Your module description
"""
from bs4 import BeautifulSoup
# importing requests
import urllib.request, urllib.parse, urllib.error
# get URL
my_req = urllib.request.urlopen("ec2-54-90-55-237.compute-1.amazonaws.com")
my_data = my_req.text
my_soup = BeautifulSoup(my_data)
for my_link in my_soup.find_all('a'):
    print(my_link.get('href'))

soup = BeautifulSoup(my_req,"html.parser")
#get a list of anchor <a> tags
tags = soup('a')
print(type(tags))
for tag in tags:
    print (tag.get('href',None))