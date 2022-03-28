
def countIPAddress(listParm):
    myd = dict(listParm)
    myIP ="192.168.0.1"
    octet = myIP[:myIP.find(".")]

myd[octet] = myd[octet] + 1
if octet in myd.keys():
    myd[octet] = myd[octet] + 1
else:
    myd[octet] =1
    print(myd)