from fabric import Connection


result = Connection(host='192.168.3.67',user="fabric",connect_kwargs={"password":"Aa123456789"}).run('uname -a', hide=True)

msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"

# print(msg.format(result))
print(result.command)

