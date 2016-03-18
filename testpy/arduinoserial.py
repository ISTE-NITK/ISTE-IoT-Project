import pygame
import serial 		#to recieve serial in and send serial out 
import time			#anything to do with keeping time/clock/etc.
import os  			#way of using operating system dependent functionality. Where in this program?			
import pickle		#serialization: putting data into a form that can be stored in a file and retrieved later
					#import cPickle as pickle for upto 1000x speed, but harder to debug as it is not 100% native Python

arr=[]
ser=serial.Serial("/dev/tty.usbserial-A9G7JH5T",9600)
print "set up serial"
time.sleep(3)			#suspends calling thread for 3 seconds to allow Arduino to initialize

ser.write('s')			#sends 's' to Arduino, which we accept and put into a conditional loop
print "sent s"

time.sleep(1)

f=open("arr.txt","wb")		#open file in write bit mode 

while(len(arr)<5000):
    rec=ser.readline()
    if (rec=='h'):
        bit=1
    elif (rec=='l')
        bit=0
    print bit+'\n'
    arr.append(bit)			#append 0 or 1 according to high or low received from Arduino 

r=raw_input()			#what is this doing?
print arr
pickle.dump(arr,f)