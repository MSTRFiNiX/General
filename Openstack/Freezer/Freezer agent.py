#!/usr/bin/python3
# _____                                                    _
#|  ___| __ ___  ___ _______ _ __    __ _  __ _  ___ _ __ | |_
#| |_ | '__/ _ \/ _ \_  / _ \ '__|  / _` |/ _` |/ _ \ '_ \| __|
#|  _|| | |  __/  __// /  __/ |    | (_| | (_| |  __/ | | | |_
#|_|  |_|  \___|\___/___\___|_|     \__,_|\__, |\___|_| |_|\__|
#                                         |___/
# Here is the new program that you can use to make use of the main freezer agent more comfterble
# You ca see all the opstion i the main panle of the this program and you can use of the main
# things as you would go.
#
#
import os
import subprocess
import sys
from colorama import Fore, Back, Style, init
init(autoreset=True)
os.system("clear")
print(Fore.RED +"""
 _____                                                    _   
|  ___| __ ___  ___ _______ _ __    __ _  __ _  ___ _ __ | |_ 
| |_ | '__/ _ \/ _ \_  / _ \ '__|  / _` |/ _` |/ _ \ '_ \| __|
|  _|| | |  __/  __// /  __/ |    | (_| | (_| |  __/ | | | |_ 
|_|  |_|  \___|\___/___\___|_|     \__,_|\__, |\___|_| |_|\__|
                                         |___/                
    """)
print(Fore.BLUE + "  1. Install freezer-agent on your system.")
print(Fore.BLUE + "  2. Make backup to swift container.")
print(Fore.BLUE + "  3. Make backup locally.")
print(Fore.BLUE + "  4. Make Authentication File (IMPORTANT!!!)")


Opstion = input(Fore.WHITE + "Give me the option: ")

if Opstion == '1' :
    os.system("clear")
    print(Fore.RED + """
     ___           _        _ _ _               _____                           
    |_ _|_ __  ___| |_ __ _| | (_)_ __   __ _  |  ___| __ ___  ___ _______ _ __ 
     | || '_ \/ __| __/ _` | | | | '_ \ / _` | | |_ | '__/ _ \/ _ \_  / _ \ '__|
     | || | | \__ \ || (_| | | | | | | | (_| | |  _|| | |  __/  __// /  __/ |   
    |___|_| |_|___/\__\__,_|_|_|_|_| |_|\__, | |_|  |_|  \___|\___/___\___|_|   
                                        |___/                                  
    """)
    #Dwonload frezer git
    os.system("git clone -b master https://github.com/openstack/freezer.git")

    #Install freezer
    print("\n Installing freezer...")
    os.system("cd freezer && pip3 install -r requirements.txt && python3 setup.py install")

    print(Fore.RED + """
        _    _ _   ____                   
       / \  | | | |  _ \  ___  _ __   ___ 
      / _ \ | | | | | | |/ _ \| '_ \ / _ \ 
     / ___ \| | | | |_| | (_) | | | |  __/
    /_/   \_\_|_| |____/ \___/|_| |_|\___|
    
    """)


if Opstion == '2':

    print(Fore.RED + """
         _   _       _                 _ _                       
        | | | |_ __ | | ___   __ _  __| (_)_ __   __ _           
        | | | | '_ \| |/ _ \ / _` |/ _` | | '_ \ / _` |          
        | |_| | |_) | | (_) | (_| | (_| | | | | | (_| |  _ _ _ _ 
         \___/| .__/|_|\___/ \__,_|\__,_|_|_| |_|\__, | (_|_|_|_)
             |_|                                |___/           
        
        """)
    pathtobackup = input("Give the path to the file that you want to make a backup of: ")
    nameofconatiner =  input("Give the name of the container you want to make backup to: ")
    backupname = input("Give the name of the backup that you are going to recall to it later: ")

    os.system("freezer-agent --path-to-backup "+ pathtobackup + " --container freezer_"+ nameofconatiner + " --backup-name " + backupname )


if Opstion == '4':
    os.system('clear')
    print(Fore.RED + """

    _         _   _                _   _           _   _             
   / \  _   _| |_| |__   ___ _ __ | |_(_) ___ __ _| |_(_) ___  _ __  
  / _ \| | | | __| '_ \ / _ \ '_ \| __| |/ __/ _` | __| |/ _ \| '_ \ 
 / ___ \ |_| | |_| | | |  __/ | | | |_| | (_| (_| | |_| | (_) | | | |
/_/   \_\__,_|\__|_| |_|\___|_| |_|\__|_|\___\__,_|\__|_|\___/|_| |_|
       """)
    print (Fore.BLUE + """Things that you aer going to need to make this authentication file:
        1.  Project domain name 
        2.  User domain name
        3.  Project name
        4.  User name
        """)



    name = input("Please enter your name: ")
    domain_name = input("Please enter your email address: ")
    project_name = input("Please enter your project name: ")
    password = input("Please enter your password: ")

    os.system("touch "+name+"_auth")
    os.system("echo 'export OS_PROJECT_DOMAIN_NAME='"+domain_name+" >> "+name+"_auth")
    os.system("echo 'export OS_USER_DOMAIN_NAME='"+domain_name+" >> "+name+"_auth")
    os.system("echo 'export OS_PASSWORD='"+password+" >> "+name+"_auth")
    os.system("echo 'export OS_name='"+domain_name+" >> "+name+"_auth")
    os.system("echo 'export OS_AUTH_URL=http://172.20.96.120:5000' >> " + name + "_auth")
    os.system("echo 'export OS_IDENTITY_API_VERSION=3' >> " + name + "_auth")
    os.environ(name +"_auth")