import sqlite3


def read_file(fileName):


# List to hold node details
nodes_list = []
# Opens the given file in read mode as 'file'
with open(fileName) as file:
# Reads all the lines to the list 'content'
content = file.readlines()
# loops through each line of the content
for eachLine in content:
# removes newline character
eachLine = eachLine.replace("\n", "")
# splits the line to individual list of words separated by ' - '
words = eachLine.split(" - ")
# stores the list to the nodes_list
nodes_list.append(words)
# returns the nodes_list
return nodes_list


def count_failed_payments(nodes_list):


# Dictionary to hold the data of failed payment nodes
failed_payment_nodes = {}
# loops through every node in the nodes_list
for eachNode in nodes_list:
# Adds the count of nodes along with node details to the dictionary
if eachNode[2].lower() == "user failed payment":
    node_data = eachNode[0] + " - " + eachNode[1]
if node_data in failed_payment_nodes.keys():
    failed_payment_nodes[node_data] += 1
else:
    failed_payment_nodes[node_data] = 1
# Displays most failed payment nodes
print("Node with most failed payments:", end="")
print("\'{}\'".format(max(failed_payment_nodes, key=failed_payment_nodes.get)))


def count_events(nodes_list):
    events_nodes = {}


# Loops throughe every node in nodes_list
for eachNode in nodes_list:
# Counts the events for each node and stores them in he dictionary
if eachNode[0] in events_nodes.keys():
    events_nodes[eachNode[0]] += 1
else:
    events_nodes[eachNode[0]] = 1
# Displays output
print("Number of events for each node: ")
for eachNode in sorted(events_nodes.keys()):
    print("{} - {}".format(eachNode, events_nodes[eachNode]))


def main():
    ''' Calls the three functions '''


nodes_list = read_file("nodes.txt")
count_failed_payments(nodes_list)
count_events(nodes_list)

main()