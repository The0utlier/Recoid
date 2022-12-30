import sys
import pyfiglet
import os
import subprocess
import random
import socket
import struct


ascii_banner = pyfiglet.figlet_format("RECOID")

print("\nWelcome to \n", ascii_banner + "Reconaissance on steroids (developed by the 0utlier).")
target = input("\nProvide target ip address: ")
option = input("\nPress 1 for port scanning, 2 for DNS analysis, 3 for WAF detection, \n4 for OSINT or 5 run all: ")

def one():
	decoy = [socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))) for i in range(0,31)]
	decoy = " ".join(decoy)

	command = f"nmap -sS -A {target} -D {decoy} --dns-servers 9.9.9.9 -Pn"
	command = list(command.split())
	print("\nRunning NMAP...\n")
	subprocess.Popen(command).communicate()

if option == "1":
	one()
	
def two():
	command = f"dnsenum {target}"
	command = list(command.split())
	print("\nRunning DNSENUM...\n\n")
	subprocess.Popen(command).communicate()

	fierce = input("Scan with fierce? y/n").lower()

	if fierce == "y":
		command = f"fierce --domain {target}"
		command = list(command.split())
		print("\nRunning FIERCE...\n\n")
		subprocess.Popen(command).communicate()

if option == "2":
	two()

def three():
	command = f"wafw00f -a {target}"
	command = list(command.split())
	print("\nRunning WAFW00F...\n\n")
	subprocess.Popen(command).communicate()

	lbd = input("Enable loadbalancer scaner? y/n").lower()
	if lbd == "y":
		command = f"lbd {target}"
		command = list(command.split())
		print("\nRunning LBD...\n\n")
		subprocess.Popen(command).communicate()

if option == "3":
	three()

def four():
	command = f"spiderfoot -s {target}"
	command = list(command.split())
	print("\nRunning SPIDERFOOT...\n\n")
	subprocess.Popen(command).communicate()

if option == "4":
	four()


if option == "5":
	one(), two(), three(), four()


else:
	print("Something went wrong")
	exit()

