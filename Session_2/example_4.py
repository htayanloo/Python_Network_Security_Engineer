#!/usr/bin/python


gateway = "192.168.0.1"
network = "192.168.3.1"
mask = "255.255.255.0"

temp = f"ip route add {network} MASK {mask} {gateway}"

print(temp)



#ip route add 192.168.3.1  MASK 255.255.255.0 192.168.0.1

# temp = "ip route add "
# temp_extra= "MASK"
#
# print(temp,network,temp_extra,mask,gateway)