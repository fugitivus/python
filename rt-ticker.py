#!/usr/bin/env python
# -*- coding: utf-8 -*-

#required:
#pip install feedparser unidecode

# Include dependencies:
import os
import sys
import time
import subprocess
import feedparser

from os import system
from time import sleep

# Helper functions:
def remove_non_ascii(s): 
	return "".join(i for i in s if ord(i)<128)

def sleep_minutes(minutes):
	sleep(minutes * 60)

# Initialize variables:
newsfeed = feedparser.parse("https://deutsch.rt.com/feeds/news/")

print ( 'Number of RSS posts :', len(newsfeed.entries) )
#entry = newsfeed.entries[1]
cmd = "python3 led-badge-11x44.py -s 8 -a 1 "
ticker = "'"
cnt = 0

# Alle Items Extrahieren:
#for value in newsfeed.entries:
#        print value.title
#        ticker += value.title
#        ticker += " *** "

# Neueste Einträge extrahieren:
while cnt < 3:
	cnt += 1
	value = newsfeed.entries[cnt]
	ticker += value.title
	ticker += " *** "	


ticker += "'"
ticker = remove_non_ascii( ticker )
cmd += ticker
#cmd = cmd.encode('ascii')


print ( cmd )
system( cmd )
