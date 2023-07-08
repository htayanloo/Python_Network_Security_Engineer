#!/usr/bin/python


def write_to_file(network):
    file = open("data.txt","a")
    file.write(f"{network['ip']},{network['mask']}\n")
    file.close()

def read_from_file():
    file = open("data.txt","r")
    networks = file.read()
    result = []
    for item in networks.splitlines():
        result.append({"ip":item.split(",")[0],"mask":item.split(",")[1]})
    file.close()
    return result

def read_from_user():
    ip = input("ip: ")
    mask = input("mask: ")

    return {"ip":ip,"mask":mask}


def main():
    print("--------------------------------------")
    print("1. add network")
    print("2. read networks")
    print("0. exit ")
    print("--------------------------------------")
    action = int(input("action : "))
    if action==1:
        network = read_from_user()
        write_to_file(network)
    elif action==2:
        netwokrs = read_from_file()
        for item in netwokrs:
            print(f"ip -> {item['ip']}  mask -> {item['mask']}")
    elif action==0:
        exit()


main()