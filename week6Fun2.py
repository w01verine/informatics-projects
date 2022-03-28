import weekSixFunction

countIPAddress(["192.168.1.0","172.10.10.0","172.10.11.1","10.10.0.0","192.10.1.1","192.10.1.0","0.0.0.0"])

def firstOctet(myd):
    myd = dict()
    myIP ="192.168.0.1"
    octet = myIP[:myIP.find(".")]
    print(octet)
    myd[octet] = myd[octet] + 1
    if octet in myd.keys():
        myd[octet] = myd[octet] + 1
    else:
        myd[octet] =1 
    print(myd)