from scapy.all import sniff, wrpcap


def save_packet(packets):
    wrpcap("/home/htayanloo/PycharmProjects/Python_Network_Security_Engineer/session_10/temp.pcap",packets)

# sniff(filter="tcp port 80",prn=packet_callback,count=100)

packets = sniff(filter="tcp and dst host 192.168.3.51 and dst port 80",count=10)

save_packet(packets)