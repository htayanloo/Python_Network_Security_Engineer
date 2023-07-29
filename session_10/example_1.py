from scapy.all import sniff
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP
from scapy.packet import Raw

show_raw= True
def packet_callback(packet):
    if packet.haslayer(HTTPRequest):

        url = packet["HTTPRequest"].Host.decode() + packet["HTTPRequest"].Path.decode()
        ip = packet[IP].src
        method = packet[HTTPRequest].Method.decode()
        if show_raw and packet.haslayer(Raw) and method=="POST":
            print(packet[Raw].load)

# sniff(filter="tcp port 80",prn=packet_callback,count=100)

sniff(filter="tcp and dst host 192.168.3.51 and dst port 80",prn=packet_callback)