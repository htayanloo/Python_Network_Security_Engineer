#!/usr/bin/python

import socket
import sys


def check_host_status(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        sock.connect((host, port))
    except ConnectionRefusedError:
        return False
    else:
        return True

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
    if check_host_status(host,item):
        print(f" host : {host}  port :{item}  open")
    else:
        print(f" host : {host}  port :{item}  close")


