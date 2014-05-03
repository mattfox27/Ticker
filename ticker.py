#!/usr/bin/python
 
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import *
from time import sleep, strftime
from datetime import datetime
 
import json
import urllib2
import time

lcd = Adafruit_CharLCDPlate()
lcd.begin(16,1)

def STAMP():
	stamp = json.load(urllib2.urlopen('https://www.bitstamp.net/api/ticker/'))
	current_price = stamp["last"]
	# > $1000 rollover, Rounds/Converts to int
	if (int(round(float(current_price))) > 1000):
		stamp_price = int(round(float(current_price)))
	else:
		stamp_price = current_price
	return stamp_price


while 1:
	lcd.clear()
	#Calls BTC function, gets time and formats.
	stamp = STAMP()
	time = datetime.now().strftime( '%x %I:%M%p\n' )
	#Displays time on first line, BTC/USD rate on next line.
	lcd.message(time)
	lcd.message( "BTC/USD: " + "$" + stamp)
	#Sleeps until next API call can be made. 
	sleep(30)