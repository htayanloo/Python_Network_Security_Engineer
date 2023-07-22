from fabric import Connection

def get_cpu_load(server_ip,username,password):
    connection = Connection(host=server_ip,user=username,connect_kwargs={"password":password})

    result = connection.run('uptime', hide=True)

    load_average = result.stdout.split("load average:")[1].strip()
    return load_average


def update(server_ip,username,password):
    connection = Connection(host=server_ip,user=username,connect_kwargs={"password":password})

    result = connection.run('sudo apt update -y', hide=True)
    print(result.stdout)
   # result = connection.run('sudo apt upgrade -y', hide=True)




#print(get_cpu_load("192.168.3.67","fabric","Aa123456789"))
update("192.168.3.67","fabric","Aa123456789")
