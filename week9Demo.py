"""
Your module description
"""
import BeautifulSoup
import urlib.request, urlib.parse, urllib.error

#http request to a site
resp = urllib.request.urlopen("https://www.cnn.com")
#use http for my website
print(type(resp))

print(resp.status)

print(resp.headers)

soup = BeautifulSoup(resp, "html.parser")
#anchor tags
tags = soup("a")
#use for loops
#img tags
tags = soup("img")

tags = soup("a")
print(type(tags))

print(tags)

for item in tags:
    if "art" in str(item).lower(): 
        print(item.get('href',None))