#!/usr/bin/python

import socket
import sys

def check_host_status(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        sock.connect((host, port))
    except ConnectionRefusedError:
        return "Close"
    else:
        return "Open"
def banner_grabbing(host, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((host,port))
        banner = s.recv(1024)
    except:
        return None
    else:
        return banner


host = sys.argv[1]
port = sys.argv[2]

def port_proccess(port):
    result = []
    try:
        result.append(int(port))
    except:
        if "," in port:
            for item in port.split(','):
                result.append(int(item))
        elif "-" in port:
            for item in range(int(port.split("-")[0]),int(port.split("-")[1])+1):
                result.append(int(item))
    return result


for item in port_proccess(port):
    banner = banner_grabbing(host,item)
    status = check_host_status(host,item)
    print(f" host : {host}  port : {item}  status: {status}  banner : {banner}")