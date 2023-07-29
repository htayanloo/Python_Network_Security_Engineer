from scapy.all import sniff, rdpcap

packets =[{"a":1,"b":2},{"a":1,"b":2},{"a":1,"b":2},{"a":1,"b":2}]
temp =[]
#
# for item in packets:
#     temp.append(item)

temp = [item["a"] for item in packets]
print(temp)