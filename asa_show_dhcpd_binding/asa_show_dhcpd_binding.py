# -*- coding: UTF-8 -*-
'''
    connect to an ASA thanks to NETMIKO. format and save result into a text file
'''
import sys
import sqlite3
from netmiko import ConnectHandler
from crayons import blue, green, white, red, yellow,magenta, cyan


def select_device():
    device=[]    
    device = {
        'device_type': 'cisco_asa',
        'ip': '192.168.100.1',
        'username': 'admin',
        'password': 'cisco'
    }                 
    return(device)

def connect(device,command):
    #connection a l ASA
    print (device)
    net_connect = ConnectHandler(**device)
    net_connect.find_prompt()
    # effectuer un show run
    output = net_connect.send_command(command)
    #print (output)
    return(output)    

if __name__ == "__main__":
    device = select_device()    
    command="show dhcpd binding"
    out_file="show_dhcpd_bind.txt"
    resultat=connect(device,command)
    #print (resultat)      
    lines=resultat.split('\n')
    for line in lines:
        if "01b8." in line: # track a specific device based on its MAC address
            print(yellow(line,bold=True))
            #print (yellow("OK DONE ( Step 2 )",bold=True))
        else:
            print(line)
    with open ( out_file , 'w' ) as f:
        f.write(resultat)        
    


    

