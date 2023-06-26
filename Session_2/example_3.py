#!/usr/bin/python

# gateway = input("gateway : ")
# network = input("network : ")
# mask = input("mask : ")

gateway = "192.168.0.1"
network = "192.168.3.1"
mask = "255.255.255.0"

temp = "ip route add %s MASK %s %s" % (mask,gateway,"192.168.10.1")

print(temp)



#ip route add 192.168.3.1  MASK 255.255.255.0 192.168.0.1

# temp = "ip route add "
# temp_extra= "MASK"
#
# print(temp,network,temp_extra,mask,gateway)