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
 
def BTC():
   stamp = json.load(urllib2.urlopen('https://www.bitstamp.net/api/ticker/'))
   current_price = stamp["last"]
   # > $1000 rollover, Rounds/Converts to int
   if (int(round(float(current_price))) > 1000):
      stamp_price = int(round(float(current_price)))
   else:
      stamp_price = current_price
   return stamp_price

def DOGE():
        cryptsy = json.load(urllib2.urlopen('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132'))
        #if cryptsy["success"] != "1":
        #                raise Exception("Cryptsy API failed!")
        current_price = cryptsy["return"]["markets"]["DOGE"]["lasttradeprice"]
        # No rollover necessary, but need to figure out how to deal with decimal places
        return current_price

#Add support for switching between currencies by using button code
while 1:
    lcd.clear()
    #Calls BTC function, gets time and formats.
    try:
           price = BTC()
    except Exception:
            lcd.message("BitStamp API failed! :(")

    time = datetime.now().strftime( '%x %I:%M%p\n' )
    #Displays time on first line, BTC/USD rate on next line
    lcd.message(time)
    lcd.message( "BTC/USD: " + "$" + price)
    #Sleeps until next API call is possible
    #Needs to be customized per API, add support next
    sleep(15)
    price = DOGE()
    time = datetime.now().strftime( '%x %I:%M%p\n' )
    #Displays time on first line, BTC/USD rate on next line
    lcd.message(time)
    lcd.message( "DOGE: " + price)
    #Sleeps until next API call is possible
    #Needs to be customized per API, add support next
    sleep(15)
    #!/usr/bin/python