# =======================================+SCRIPT BY Nitiraj Kulkarni+==============================================
#
# ==========================================+date : 2020/5/28+===============================================

import sys
import os
import time
import subprocess

import platform


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 1000)


slowprint("[!] Starting : ")
time.sleep(0.9)
os.system('')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)


slowprint("    \033[91mThe Easy")
print('''                              
       
             _.-;;-._
      '-..-'|   ||   |
      '-..-'|_.-;;-._|
      '-..-'|   ||   |
      '-..-'|_.-''-._|
                            INFORMATION COLLECTOR
                                                                                         ''')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)


slowprint('''\033[1;31m \033[91m ''')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)


slowprint("\t\t                                                   \033[93mBy :Nitiraj kulkarni")

print('')
print("Press Enter to collect info about this device")

nitiraj = input("\033[92m \033[96m==>")


slowprint("\033[97m")
print("=" * 40, "System Information", "=" * 40)
uname = platform.uname()
print('')
print(f"System: {uname.system}")
print('')
print(f"Node Name: {uname.node}")
print('')
print(f"Release: {uname.release}")
print('')
print(f"Version: {uname.version}")
print('')
print(f"Machine: {uname.machine}")
print('')
print(f"Processor: {uname.processor}")

print(" ")
print(" ")

import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("=" * 40, "IP and USER Information", "=" * 40)
import re, uuid

print('')
print("MAC Address: ", end="")
print('')
print(':'.join(re.findall('..', '%012x' % uuid.getnode())))
print('')
print("Computer Name is:" + hostname)
print('')
print("Computer IP Address is:" + IPAddr)
print('')
print("...............................................................................................................")

print("")
print("")
print("Text file is generated")
print("")
print("FOR DONATIONS: https://www.paypal.me/VasudeoKulkarni ")
print("")
input('Press ENTER to exit')

my_file = open("System_Info.txt ", "w+")
my_file.write(f"System: {uname.system}");

print('')
my_file.write(
    f"Node Name: {uname.node}"
    f"\n"f"System: {uname.system}"
    f"\n"f"Release: {uname.release}"
    f"\n"f"Version: {uname.version}"
    f"\n"f"Machine: {uname.machine}"
    f"\n"f"Processor: {uname.processor}"
    f"\nComputer Name is:" + hostname)

#my_file = open("IP & Network_Info.txt", "w+")
#my_file.write(f"System: {uname.system}");








