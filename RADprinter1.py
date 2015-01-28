# Created By: ASIS&T@UBC
# Title: RAD device
# Desc: Prints random book recommendations from a CSV
# Date: 2014
#


from random import randrange

import csv
import textwrap
import printer

#create hashmap with csv file contents
hashmap = []

#FILE PATH SHOULD REFLECT ACTUAL FILE DIRECTORY
docpath = '/home/pi/py-thermal-printer/booklist1.csv'

with open(docpath,'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|')
    for row in spamreader:
        hashmap.append(row)

#code for button connection
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while True:
    if(GPIO.input(23) == False):
        #generate random number
        random_num = randrange(0,len(hashmap))

	#print random line from csv
        book = hashmap[random_num]

        #formatting for printing the line
        wrapped_title = textwrap.fill(book[0],32)
        wrapped_author = textwrap.fill(book[1],32)

        p=printer.ThermalPrinter(serialport="/dev/ttyAMA0")    
        p.print_text("\nHey book lovers! How's it going?\n")
        p.justify("C")
        p.print_text("Check out")
        p.linefeed()
        p.justify("C")
        p.underline_on()
        p.print_text(wrapped_title)
        p.underline_off()
        p.linefeed()
        p.justify("C")
        p.print_text("by ")
        p.underline_on()
        p.print_text(wrapped_author)
        p.underline_off()
        p.linefeed()
        p.justify()
        if(len(book) > 2):
            wrapped_desc = textwrap.fill(book[2],32)
            p.print_text(wrapped_desc)
        p.linefeed()
        p.linefeed()
        p.linefeed()
        p.linefeed()
        p.linefeed()
        
	sleep(2)
        sleep(0.25)
