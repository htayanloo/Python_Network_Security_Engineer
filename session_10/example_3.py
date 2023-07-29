from scapy.all import sniff, rdpcap



packets = rdpcap("/home/htayanloo/PycharmProjects/Python_Network_Security_Engineer/session_10/temp.pcap")

for packet in packets:
    print(packet.summary())