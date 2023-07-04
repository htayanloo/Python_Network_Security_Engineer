#1/usr/bin/python


# file = open("/home/htayanloo/PycharmProjects/Python_Network_Security_Engineer/Session_4/data.txt","")


# file = open("data.txt","w")

# file_w = open("data.txt","a")
# file_w.write("hello python class_2\n")
# file_w.close()

col_num = int(input("select col for view in log :"))
file_r = open("data.txt","r")

logs = file_r.read()

print(logs.split()[col_num])


