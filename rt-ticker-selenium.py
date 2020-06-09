#!/usr/bin/env python
# -*- coding: utf-8 -*-

#required:
#firefox-gecko-driver has to be installed...
#pip install selenium unidecode
#https://best-proxy.com/english/index.php

# Include dependencies:
import sys
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# Helper functions:
def remove_non_ascii(s): return "".join(i for i in s if ord(i)<128)

# Initialize variables:
ticker = ""

# Firefox mit Selenium Initialisieren:
options = Options()
options.headless = True
options.add_argument('--no-sandbox')
#options.binary = "/usr/bin/firefox"
browser = webdriver.Firefox(options=options)
browser.get('https://deutsch.rt.com/newsticker/')
#print ("Headless Firefox Initialized")
#print ("Waiting for site to be fully loaded..")
#assert 'Kurzmeldungen' in browser.title

# Items Extrahieren:
elem = browser.find_elements_by_class_name('link_hover_red')
for value in elem:
        print (value.text)
        ticker+=value.text
        ticker+=" --- "

# Close Firefox & Selenium:
#print ("Headless Firefox was closed.")
browser.quit()

#print ("Nachrichtentext:")
print (ticker)

# Send Ticker to LED-Badge:
#python3 led-badge-11x44.py -s 8 -a 1 ticker
#remove_non_ascii(ticker)
#ticker = "Hallo Welt!!!"
#subprocess.Popen("sudo python3 led-badge-11x44.py -s 8 -a 1 HalloWelt", shell=True)
