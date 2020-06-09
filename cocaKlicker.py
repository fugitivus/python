#!/usr/bin/env python
# -*- coding: utf-8 -*-

#required:
#firefox-gecko-driver has to be installed...
#pip install selenium
#https://best-proxy.com/english/index.php

import sys
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Parse Arguments:
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--code", help="MC-Donalds Gutscheincode", type=str)
parser.add_argument("-p", "--proxy", help="Proxy-Server (Optional)", type=str)
args = parser.parse_args()

def print_help():
	print("usage: cokaKlicker.py -c <CODE> -p <PROXY(Optional)>")
	sys.exit(0)

if args.code: 
	gutscheincode = args.code
else:
	print_help()
	
if args.proxy:
	proxyserver = args.proxy
	webdriver.DesiredCapabilities.FIREFOX['proxy']={
		"httpProxy":proxyserver,
		"sslProxy":proxyserver,
		"proxyType":"MANUAL"
	}


#Start Selenium webdriver:
#browser = webdriver.PhantomJS()
#browser.save_screenshot('screen.png')
browser = webdriver.Firefox()
#browser.get('https://mcdonalds.de/deinfeedback')
browser.get('https://mcdonalds.fast-insight.com/de/de')
time.sleep(5)




assert 'McDonald' in browser.title
elem = browser.find_element_by_id('receiptCode') 
elem.send_keys(gutscheincode + Keys.RETURN)


time.sleep(10)
print("Bitte beurteile Deine Gesamtzufriedenheit basierend auf der Erfahrung Deines letzten Besuches.")
assert 'Gesamt' in browser.page_source
time.sleep(2)
elem = browser.find_element_by_class_name('rating')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Wie zufrieden warst Du mit der Freundlichkeit unserer Mitarbeiter?")
time.sleep(1)
assert 'Mitarbeiter' in browser.page_source
elem = browser.find_element_by_class_name('rating')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Du warst mit der Freundlichkeit unserer Mitarbeiter nicht zufrieden")
time.sleep(1)
assert 'verbessern' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Wie zufrieden warst Du mit der Schnelligkeit unseres Services?")
time.sleep(1)
assert 'Services' in browser.page_source
elem = browser.find_element_by_class_name('rating')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Du warst mit der Schnelligkeit nicht zufrieden. Was hat aus Deiner Sicht zu lange gedauert?")
time.sleep(1)
assert 'Schnelligkeit' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Wie zufrieden warst du mit den Erhaltenen Speisen / Getränke?")
time.sleep(1)
assert 'Speisen' in browser.page_source
elem = browser.find_element_by_class_name('rating')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Du warst mit der Qualität der erhaltenen Speisen und Getränke nicht zufrieden. Welcher der folgenden Punkte beschreibt...")
time.sleep(1)
assert 'beschreibt' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Wie zufrieden warst Du mit der Sauberkeit des Restaurants?")
time.sleep(1)
assert 'Sauberkeit' in browser.page_source
elem = browser.find_element_by_class_name('rating')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Du warst mit der Sauberkeit nicht zufrieden. Welche Bereiche im Restaurant betraf dies?")
time.sleep(1)
assert 'Bereiche' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Wurde Deine Bestellung ordnungsgemäß zusammengestellt und bearbeitet?")
time.sleep(1)
assert 'bearbeitet' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Wie zufrieden warst Du mit dem Geschmack Deiner Speisen?")
time.sleep(1)
assert 'Geschmack' in browser.page_source
elem = browser.find_element_by_class_name('rating')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Wie stark hast Du Dich während des Besuchs als Gast wertgeschätzt gefühlt?")
time.sleep(1)
assert 'Besuchs' in browser.page_source
elem = browser.find_element_by_class_name('rating')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Verlief der Besuch in irgendeinem Punkt nicht zu Deiner Zufriedenheit?")
time.sleep(1)
assert 'irgendeinem' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Womit genau warst Du unzufrieden?")
time.sleep(1)
assert 'unzufrieden' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Wie wahrscheinlich würdest Du uns auf einer Skala von 0-10 an Freunde und Bekannte weiterempfehlen?")
time.sleep(1)
assert 'wahrscheinlich' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Dein letzter Besuch bei uns ist nicht gut verlaufen, was können wir aus Deiner Sicht besser machen?")
time.sleep(1)
assert 'verlaufen' in browser.page_source
elem = browser.find_element_by_css_selector('input.politeText.required.requiredtrim')
elem.send_keys('bessere Preise....' + Keys.RETURN)

print("Du bist?")
time.sleep(1)
assert 'bist' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Bitte nenne uns dein Alter")
time.sleep(1)
assert 'Alter' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Für wie viele Personen, einschließlich Dir und all Deinen Begleitern/Innen, hast Du heute bezahlt?")
time.sleep(1)
assert 'Personen' in browser.page_source
elem = browser.find_element_by_css_selector('select.required')
elem.send_keys(Keys.DOWN + Keys.DOWN + Keys.ENTER)
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Für wie viele Kinder (unter 14 Jahren) hast Du heute bezahlt?")
time.sleep(1)
assert 'Kinder' in browser.page_source
elem = browser.find_element_by_css_selector('select.required')
elem.send_keys(Keys.DOWN + Keys.DOWN + Keys.ENTER)
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Was war der Besuch bei McDonald's heute für Dich?")
time.sleep(1)
assert 'Besuch' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Wie oft besuchst Du ein McDonald's Restaurant?")
time.sleep(1)
assert 'McDonald' in browser.page_source
elem = browser.find_element_by_class_name('opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

print("Du warst bei Deinem letzten Besuch nicht ganz zufrieden. Möchtest Du kontaktiert werden?")
time.sleep(1)
assert 'kontaktiert' in browser.page_source
elem = browser.find_element_by_css_selector("div.option:nth-child(2)")
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()

#print("Bitte nenne uns deinen Namen?")
#time.sleep(1)
#assert 'Bitte' in browser.page_source
#elem = browser.find_element_by_css_selector('input.politeText.required.requiredtrim')
#elem.send_keys('Bernd das Brot' + Keys.RETURN)

#print("Bitte nenne uns deine E-Mail Adresse")
#time.sleep(1)
#assert 'Bitte' in browser.page_source
#elem = browser.find_element_by_css_selector('input.politeText.required.requiredtrim')
#elem.send_keys('bernd@brot.de' + Keys.RETURN)

#print("Bitte nenne uns deine Telefonnummer")
#time.sleep(1)
#assert 'Bitte' in browser.page_source
#elem = browser.find_element_by_css_selector('input.politeText.required.requiredtrim')
#elem.send_keys('00230265792' + Keys.RETURN)

print("Bitte bestätige unsere Datenschutzbestimmungen.")
time.sleep(1)
assert 'Bitte' in browser.page_source
elem = browser.find_element_by_css_selector('span.opt-text')
elem.click()
elem = browser.find_element_by_id('next-sbj-btn')  
elem.click()





#elem.send_keys('Irgendeintext' + Keys.RETURN)
#browser.quit()
