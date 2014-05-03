#!/usr/bin/python

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import * 
from time import sleep, strftime
from datetime import datetime
import pycurl
from StringIO import StringIO
import time

lcd = Adafruit_CharLCDPlate()
def autoscroll(self):
        """ This will 'right justify' text from the cursor """
        self.displaymode |= self.LCD_ENTRYSHIFTINCREMENT
        self.write(self.LCD_ENTRYMODESET | self.displaymode)
# The DENSITRON 2 617ASNG0441 is an 8x2 LCD, even though it looks like 16x1
lcd.begin(16,1)

count = 0
cont = 1
lastCheckTime = 0;
stockQuotes = ""

while cont:
   nowTime = time.time()
   if (nowTime - lastCheckTime > 30):
      # Call Yahoo every 30 seconds, don't overload it, get results
      storage = StringIO()
      c = pycurl.Curl()
      c.setopt(c.URL, 'http://download.finance.yahoo.com/d/quotes.csv?s=^IXIC&f=sghn')
      c.setopt(c.WRITEFUNCTION, storage.write)
      c.perform()
      stockQuotes = storage.getvalue()
      print "Current Time :", time.asctime(time.localtime(nowTime))
      print "Last checked time :", time.asctime(time.localtime(lastCheckTime))
      print stockQuotes
      lastCheckTime = nowTime
   lcd.clear()
   lcd.scrollDisplayLeft()
   lcd.message(stockQuotes)
   sleep(2)
