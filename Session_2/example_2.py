#!/usr/bin/python

# a= ["111","222","333","4444"]
temp = "ip  route  add  192.168.100.0  MASK  255.255.255.0  192.168.2.1"
temp_list = temp.split("MASK")
print(temp_list)
print(temp_list[1])