from ipaddress import *

net = ip_network('11.92.135.56/255.224.0.0', 0)

c = 0
for ip in net:
    #print(ip)
    c += 1
    if c == 2097152 - 1:
        print(ip)

print(c)