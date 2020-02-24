#!/usr/bin/python3
# coding: utf-8

import shellcolor
import csv
import sys

from shellcolor import *

def python_check_version():
	if sys.version_info<(3,0,0):
	  sys.stderr.write("You need python 3.0 or later to run this script\n")
	  exit(1)

def csv_read_test():
	print(fg_red,"csv_read_test():", fg_normal)
	with open('csv-read-test.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=';')
		for row in readCSV:
				#print(row)
				print(row[0], row[1], row[2])
				if row[0] == "Doe":
					print (fg_red,"DOE FOUND!!!",fg_normal)
	
def csv_read_mapping_test():
	print(fg_red,"csv_read_mapping_test():", fg_normal)
	with open('csv-read-test.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=';')
		list_nName = []
		list_vName = []
		list_gDate = []
		list_gesch = []
		
		for row in readCSV:
			nName = row[1]
			vName = row[0]
			gDate = row[2]
			gesch = row[3]
			
			list_nName.append(nName)
			list_vName.append(vName)
			list_gDate.append(gDate)
			list_gesch.append(gesch)

		print(list_vName)
		print(list_nName)
		print(list_gDate)
		print(list_gesch)
		print("Date of Doe", list_gDate[list_nName.index("Doe")])
		print("vName of Doe", list_vName[list_nName.index("Doe")])

def csv_dict_reader_test():
	print(fg_red,"csv_dict_reader_test():", fg_normal)
	with open('csv-read-test.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=';')
		for row in reader:
			print(row['Nachname'],row['Geschlecht'])

def csv_dict_writer_create_test():
	print(fg_red,"csv_dict_writer_create_test():", fg_normal)
	
	
	with open('csv-write-test.csv', 'w') as csvfile:

		fnames = ['Vorname', 'Nachname','Geburtsdatum', 'Geschlecht']
		writer = csv.DictWriter(csvfile, fieldnames=fnames, delimiter=';')    

		writer.writeheader()
		writer.writerow({'Vorname' : 'John', 'Nachname': 'Smith','Geburtsdatum': '17.09.1980', 'Geschlecht': 'Männlich'})
		writer.writerow({'Vorname' : 'Jane', 'Nachname': 'Doe','Geburtsdatum': '19.01.1983', 'Geschlecht': 'Weiblich'})
		writer.writerow({'Vorname' : 'Nathan', 'Nachname': 'Blacksmith','Geburtsdatum': '03.05.2000', 'Geschlecht': 'Männlich'})
					
def csv_dict_writer_append_test():
	print(fg_red,"csv_dict_writer_create_test():", fg_normal)
	
	
	with open('csv-write-test.csv', 'a') as csvfile:
		fnames = ['Vorname', 'Nachname','Geburtsdatum', 'Geschlecht']
		writer = csv.DictWriter(csvfile, fieldnames=fnames, delimiter=';')    

		writer.writerow({'Vorname' : 'John', 'Nachname': 'Smith','Geburtsdatum': '17.09.1980', 'Geschlecht': 'Männlich'})
		writer.writerow({'Vorname' : 'Jane', 'Nachname': 'Doe','Geburtsdatum': '19.01.1983', 'Geschlecht': 'Weiblich'})
		writer.writerow({'Vorname' : 'Nathan', 'Nachname': 'Blacksmith','Geburtsdatum': '03.05.2000', 'Geschlecht': 'Männlich'})
		
		
####test main csv functions:
python_check_version()
csv_read_test()
csv_read_mapping_test()
csv_dict_reader_test()
csv_dict_writer_create_test()
csv_dict_writer_append_test()


