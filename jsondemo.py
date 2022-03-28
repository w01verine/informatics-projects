import json

#read json data from file
myjson = open("isi.json","r")

jsonRawData = myjson.read()

#print list of dictionaries
#print (jsonRawData)

#create python json object using json and loads (load string) functiont
jsonObject = json.loads(jsonRawData)

#get list of professors and classrooms from json.    
for item in jsonObject:
    print(item["Name"])
    print (item["Email"])
    print (item["Office"])
    
#classrooms
#read json data from file
myjson = open("classroom.json","r")

jsonRawData = myjson.read()
myjson.close()
#print list of dictionaries
#print (jsonRawData)

#create python json object using json and loads (load string) functiont
jsonObject = json.loads(jsonRawData)
#print  type(jsonObject)

#get list of professors and classrooms from json.    
for item in jsonObject:
    print(item["Building"])
    print (item["Room"])
    print (item["Level"])