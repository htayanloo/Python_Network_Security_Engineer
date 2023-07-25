from netmiko import ConnectHandler


mikrotik_router = {
    "device_type":"cisco",
    "ip":"192.168.3.58",
    "username":"admin",
    "password":""
}

connection = ConnectHandler(**mikrotik_router)

output = connection.send_command("ip arp print")
print(output)

# file = open("mikrotik_1.rsc","a+")
# file.write(output)
# file.close()
connection.disconnect()


