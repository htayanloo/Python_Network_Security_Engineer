#!/usr/bin/python

import socket
def check_host_status(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((host, port))
    except ConnectionRefusedError:
        return False
    else:
        return True

host = "192.168.101.1"
port = 21

if check_host_status(host,port):
    print(f" host : {host}  port :{port}  open")
else:
    print(f" host : {host}  port :{port}  close")


