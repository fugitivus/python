#!/usr/bin/python3
# coding: utf-8

import sys
import math
import csv

from math import sin # man kann mit * auch alles importieren





def math_test(eingabe):
	lf_var1 = 10.10
	lf_var2 = 10.10
	lf_var3 = lf_var1 + lf_var2

	print ("Math Long-Float")
	print ("Var1: ", lf_var1)
	print ("Var2: ", lf_var2)
	print ("Var3: ", lf_var3)
	print ("PI: ", math.pi)
	print ("sin(PI/2): ",sin(math.pi/2))
	print ("cos(PI/2): ",math.cos(math.pi/2))
	print ("sqrt(9): ", math.sqrt(9))

	return eingabe

def string_test():
	print ("Strings: ")
	eingabe=input("Gebens sie etwas ein: ")

	if eingabe == "Test":
		print ("Eingabe war richtig: ",eingabe)
	elif eingabe == "Test2":
		print ("Eingabe war richtig: ",eingabe)				
	else:
		print ("Eingabe war falsch: ", eingabe)
		
	return eingabe
def saghallo():
	print ('Hallo, hier spricht meinmodul.')

version = '0.1'

# Ende von meinmodul.py
				
