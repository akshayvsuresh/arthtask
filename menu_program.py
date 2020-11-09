import os
from getpass import getpass
import subprocess as sp
from linux_cmd import *
from aws_code import *
from docker import *
from webserver import *
from hadoop import * 

Password= "pw"

while True:
	os.system("tput setaf 5")
	pw = getpass("\n\tEnter your password: ")
	if pw == Password:
		print("\n\tContinue.....")
		os.system("sleep 1")
		break
	else:
		print("\tIncorrect password!\n")


while True:
	os.system("clear")
	os.system("tput setaf 7")
	print("--------------Welcome to Python automation Menu Program--------------"
	os.system("tput setaf 1")
	print("""
	\t\tPress 1 : For basic linux command
	\t\tPress 2 : For using AWS services
	\t\tPress 3 : For Docker
	\t\tPress 4 : For Configure WebServer
        \t\tPress 5 : For Hadoop
	""")
	
	os.system("tput setaf 2")
	x = input("Enter your choice: ")
	os.system("tput setaf 7")
	
	if int(x) == 1:
    		lxcmd()
    	elif int(x) == 2:
		aws()
	elif int(x) == 3:
   		selectopt()
        elif int(x) == 4:
		web()
        elif int(x) == 5:
                hadoop ()
    		
	else:
		print(" Choose the valid option ")

