#!/usr/bin/python3
# coding: utf-8

import shellcolor
import csv
import sys

from shellcolor import *

list_in = []

def python_check_version():
	if sys.version_info<(3,0,0):
	  sys.stderr.write("You need python 3.0 or later to run this script\n")
	  exit(1)
	  
def test_file_read():
	count=0
	
	print(fg_red,"test_file_read():", fg_normal)
	with open('file-read-test.txt', 'r') as readfile:
		for row in readfile:
			count += 1
			print ("Zeile: ",count," ", row, end='')
			list_in.append(row)
			
def test_file_write():
	count=0
	
	print(fg_red,"\ntest_file_write():", fg_normal)
	with open('file-write-test.txt', 'w') as writefile:
		for row in list_in:
			count += 1
			print ("Zeile: ",count," ", row, end='')
			writefile.write(row)	

def test_file_append():
	count=0
	
	print(fg_red,"\ntest_file_append():", fg_normal)
	with open('file-write-test.txt', 'a') as appendfile:
		for row in list_in:
			count += 1
			print ("Zeile: ",count," ", row, end='')
			#appendfile.write(row[:-1])#<-withiut newline	
			appendfile.write(row)

#Main Part:	  
python_check_version()
test_file_read()
test_file_write()
test_file_append()




