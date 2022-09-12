"""
Each problem below must be solved using at least one function.

Log file is located in the comments



1. Which node had the most "failed payment" records? Display the node and number of
records in the output.


2. How many events does each "node" have in the logs.txt file? Display the node and
the number of events for the node in the output.


3. What are the IP addresses in the logs.txt file? List each IP address in the output once
with no repeating or duplicate IP addresses. The output must be the unique list of IP
addresses.


4. What are the event messages found in the logs.txt file? List each message in the output
once with no repeating or duplicate messages. The output must be the unique list of
messages. An example of a log message is "User Failed Payment."
"""
# read .txt file

f = open('Applog.txt', "r")

nodes = []
IP = []
message = []

for line in f.readlines():  # take one line at a time
    nodes.append(line[1:6])  # extract the node
    IP.append(line.split('-')[1].strip())  # split based on - and then take the IP on 1 index and then remove spaces.
    message.append(
        line.split('-')[2].strip())  # # split based on - and then take the message on 2 index, then remove spaces.
import pandas as pd

df = pd.DataFrame({
    'Nodes': nodes,
    'IPs': IP,
    'Message': message
})

df.head()

print(df[df['Message'] == 'User Failed Payment'].groupby('Nodes').count()['Message'].idxmax(),
      df[df['Message'] == 'User Failed Payment'].groupby('Nodes').count()['Message'].max())

# Explanation:
# df[df['Message'] == 'User Failed Payment'] simply filters the rows with failed payments.
# groupby('Nodes') simply groups all rows across the nodes.
# count()['Message'] counts the grouped messages across nodes.
# idxmax() returns the index of the max values which will be the node.
# max() returns the max value which will be the max number of failed payments.

# output will be node5 993


#### 2.

df.groupby(['Nodes', 'Message']).count()

# Explanation
# groupby method simply groups across Nodes and Messages and then count just counts the number of rows which will be the
# count of messages across nodes.

#### 3.

df['IPs'].drop_duplicates().values  # we just drop the duplicates and extract values

#### 4.

df['Message'].drop_duplicates().values  # we just drop the duplicates and extract values