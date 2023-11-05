#!/usr/bin/python

import argparse

from src import ddos


def main():
    parser = argparse.ArgumentParser(description="DDoS Proof of concept")
    parser.add_argument('-t', '--target', help="Attack target IP address")
    parser.add_argument('-p', '--port', help="Port to attack")
    parser.add_argument('-i', '--ipaddress', help="Fake ip address")

    args = parser.parse_args(ddos)



if __name__ == "__main__":
    main()
