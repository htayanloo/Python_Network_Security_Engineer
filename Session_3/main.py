#!/usr/bin/python
import os

## first solution
routes_by_network = {
    "192.168.0.0/24":[{"gateway":"192.168.5.1"},{"gateway":"192.168.5.1"}],

    "192.168.1.0/24": {"192.168.5.1","192.168.5.1"},

    "192.168.2.0/24": {"192.168.5.1":"gateway","192.168.7.1":"gateway"},
}


## second solution
route_by_gateway = {
    "192.168.8.1":{"192.168.5.0/24","192.168.6.0/24"}

}

routes = [
    {"network":"192.168.0.0/24","gateway":"192.168.5.1"},
    {"network":"192.168.6.0/24","gateway":"192.168.5.1"},
]

while True:

    os.system("clear")
    print("--------------------")
    print("1. add route")
    print("2. show route")
    print("3. search route")
    print("0. exit")
    print("--------------------")
    action = int(input("please select action: "))
    if action == 1:
        os.system("clear")
        network = input("network:")
        mask = input("mask:")
        gateway = input("gateway:")

        # route = {"network":network,"mask":mask,"gateway":gateway}
        # routes.append(route)

        routes.append({"network":network,"mask":mask,"gateway":gateway})

    elif action == 2:
        os.system("clear")
        print("network          mask           gateway")
        for item in routes:
            print(f"{item['network']}   {item['mask']}     {item['gateway']}")

        noaction = input()
    elif action == 3:
        os.system("clear")
        network = input("insert network for search:")
        found = False
        for item in routes:
            print("AA")
            if item["network"] == network:
                found = True
                print(f"Found your network :: {item['network']}   {item['mask']}     {item['gateway']} ")

        if found == False:
            print("Not Found")
        noaction = input()
    elif action== 0:
        break



