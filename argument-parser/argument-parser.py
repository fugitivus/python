#!/usr/bin/python3
# coding: utf-8

import shellcolor
import argparse
import sys

from shellcolor import *

def python_check_version():
	if sys.version_info<(3,0,0):
	  sys.stderr.write("You need python 3.0 or later to run this script\n")
	  exit(1)

def check_arguments():
	parser = argparse.ArgumentParser(description="Hilfe -> Beschreibung als Text")
	group = parser.add_mutually_exclusive_group()

	group.add_argument("-q", "--quiet", action="store_true", help="the base")
	parser.add_argument("--echo", help="Echo Hilfetext")
	parser.add_argument("--dump", "-d", type=int, help="the base")
	parser.add_argument("--verbose", "-v", help="Verbose Hilfetext", action="store_true")

	args = parser.parse_args()
	
	if(args):print("HEEEELLLLP....", args)	
	if(args.echo != None):print("Argument von echo: ",args.echo)
	if(args.verbose):print("Verbose wurde ausgesucht...") 
	
	return args.echo, args.verbose
		
####test main argparse functions:
python_check_version()
shellcolor.cls()
print("Return ",check_arguments())



