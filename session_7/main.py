#!/usr/bin/python

import socket
import sys
import concurrent.futures

CORE_CPU_THREAD_COUNT = 8
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


def full_scan(port):
    host = "192.168.101.1"
    status = check_host_status(host,port)

    if status =="Open":
        banner = banner_grabbing(host, port)
        print(f" host : {host}  port : {port}  status: {status}  banner : {banner}")# ----------------------------------------------------

host = sys.argv[1]
port = sys.argv[2]


ports = []

for item in port_proccess(port):
    ports.append(item)
    #print(f" host : {host}  port : {item}  status: {status}  banner : {banner}")





with concurrent.futures.ThreadPoolExecutor(CORE_CPU_THREAD_COUNT) as executor:
    results = executor.map(full_scan,ports)
    #count = results['count']

    #print(f"proccess {count} scan")
