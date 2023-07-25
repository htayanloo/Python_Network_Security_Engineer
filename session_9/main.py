class SwitchCiscoManagement():
    def check_ip(self,ip):
        if ip:
            return True
        else:
            return False

    def send_command(self,port_name):
        NotImplemented



class SwitchCiscoManagementMikrotik(SwitchCiscoManagement):
    def check_ip(self, ip):
        print("ALI")

    def send_command(self,port_name):
        return "success"



temp = SwitchCiscoManagementMikrotik()

print(temp.disable_port_security())