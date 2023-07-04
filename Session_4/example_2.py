#1/usr/bin/python

def check_host_port(host,port=80):

    if host == "192.168.0.1" and port == 8000:
        return True
    else:
        return False



# result = check_host_port(host="192.168.0.3",port=8000)
#
# result = check_host_port("192.168.0.3",8000)


# host = input("host :")
# port = input("port :")
#
argument = {"host":host,"port":port}

# result = check_host_port(host=argument["host"],port=argument["port"])

result = check_host_port(**argument)


# check_host_port(host="192.168.0.1")


def show_routes(routes):
    final_list = []
    for item in routes:
        final_list.append(int(item)+1)
    return final_list


result = show_routes(routes=["1","2","3"])
print(result)

print(show_routes(routes=["1","2","3"]))