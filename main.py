# import sys
import os
import random
import platform
import argparse
import threading
import socket

# TODO: Read docs on time, os, random, and platform
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


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes1 = random.randbytes(2000)
bytes2 = random.randbytes(2900)
system = platform.uname()[0]


def check_os():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Unix':
        os.system("clear")


# Just added stupid infinite loop to shut up PyCharm complaints
# The loop is stupid and doesn't work, but it is just filler

def ddos(target, port, ipaddress):
    try:
        while True:
            num = 0
            num2 = 1
            comp = num < num2
            print(f"{comp}, infinite loop son")
    except:
        print("some more dummy text yo")


for i in range(150):
    thread = threading.Thread(target=ddos)
    thread.start()


def main():
    parser = argparse.ArgumentParser(description="DDoS Proof of concept")
    parser.add_argument('-t', '--target', help="Attack target IP address")
    parser.add_argument('-p', '--port', help="Port to attack")
    parser.add_argument('-i', '--ipaddress', help="Fake ip address")

    args = parser.parse_args()

    ddos(args.target, args.port, args.ipaddress)


if __name__ == "__main__":
    main()
