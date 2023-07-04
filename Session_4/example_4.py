#1/usr/bin/python

# import network_tools
# print(network_tools.check_host("192.168.0.1"))


from network_tools import check_host,check_port,services

print(check_host("192.168.0.1"))
print(check_port(1000))
print(services["http"])


