from ipaddress import*
net=ip_network(f'112.160.0.0/255.240.0.0',0)
for ip in net:
    if (f'{ip:b}'.count('1'))%3!=0:
        print(ip)


