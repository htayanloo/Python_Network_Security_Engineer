import ipaddress

# try:
#     netid = ipaddress.ip_network("192.168.1.0/29")
# except:
#     print("input is not net id ")
# else:
#     for item in netid:
#         print(item)

#
# address = ipaddress.ip_address("192.168.1.0")
# print(address.is_loopback)

ip = ipaddress.ip_network("10.0.0.0/16")
print(list(ip.hosts()))