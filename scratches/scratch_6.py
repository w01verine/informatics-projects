# Read the file
f = open('Applog.txt', "r")

# Seperate the data into lists
nodes = []
IP = []
message = []

# take one line at a time
for line in f.readlines():
    # extract the node
    nodes.append(line[1:6])
    # extract the IP adresses and remove spaces
    IP.append(line.split('-')[1].strip())
    # split based on - and then take the message on 2 index and remove spaces
    message.append(line.split('-')[2].strip())

#list
mylist = ['nodes']

#takes values from list and create a dictionary with the list value as a key and
#the number of times it is repeated as their values
def counts(mylist):
d = dict()
for value in mylist:
    if value not in d:
        d[value] = 1
    else:
        d[value] +=1

return d

#prints the keys and their vaules
def print_votes(dic):
    for c in dic:
        print(c +' - voted', dic[c], 'times')







 print('c' +' - voted', dic[c], 'times')












print_votes(votes(mylist))