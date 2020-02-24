#!/usr/bin/python3
# coding: utf-8

import math
import random
import modtest
import argparse
import subprocess
import shellcolor
import platform
import os

from random import *
from shellcolor import *
from modtest import *
#from tinker import *
	
####Einfach mal ein Testmodul:
#rw1=modtest.math_test(max(10,100,199,99))
#rw2=modtest.string_test()
#print ("Rückgabewerte: ", rw1, " ", rw2)

####Test von Betriebssystem Funktionen:
#betrsys=platform.system()
#vers=platform.version()
#print ("Betriebssystem: ", betrsys, " ", vers)

####Zufallszahlen:
#zahl1=randint(1,100)
#print ("Random: ", zahl1)

####System Calls:
#testvar=os.system("ls -al")
#print "Testvar:\n",testvar
#testvar=os.popen("ls -al").readlines()
#print (fg_white,"Testvar: ",testvar[1], fg_normal)
#print ("Testvar: ",testvar[2])
#print ("Testvar: ",testvar[3])
#print ("Elemente:",len(testvar))

####Csv Dateien:
csv_read_test()
csv_read_mapping_test()



