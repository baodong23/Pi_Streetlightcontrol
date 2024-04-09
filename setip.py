import os

def IPconfig(IP: str, IPSV: str, DNS: str):

    config_lines = [
        'interface wlan0',
        '\tstatic ip_address={}'.format(IP),
        '\tstatic routers={}'.format(IPSV),
        '\tstatic domain_name_servers={}'.format(DNS),
        '\tinterface eth0',
        '\tstatic ip_address=192.168.9.150'
        ]
    config = '\n'.join(config_lines)
    
    #give access and writing. may have to do this manually beforehand
    os.popen("sudo chmod a+w /etc/dhcpcd.conf")
    
    #writing to file
    with open("/etc/dhcpcd.conf", "w") as ipconfig:
        ipconfig.write(config)
        
    os.popen("sudo reboot")