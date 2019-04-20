#!/usr/bin/env python3.5
import socket
import serial
from time import time, sleep
import socket
from struct import pack, unpack
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
mode_pin = [23, 24]
aux_pin = 18
for pin in mode_pin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
GPIO.setup(aux_pin, GPIO.IN)

rf_uart = serial.Serial('/dev/ttyAMA0', 19200, timeout=0.1)
GPIO.output(mode_pin[0], 0)                    #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
GPIO.output(mode_pin[1], 0)                    #then these two lines will send low logic to both which puts the module in transmit mode 0

def packDEEZNUTZ(): #object to bytes
    try:
        return pack('7i', int(1), int(2), int(3), int(4), int(5), int(6), int(7))

    except:
        print("Error in D")

def unpackGPS(gps):
    return unpack("2i", gps)

def unpackDEEZNUTZ(message): #object to bytes
    #try:
    data = unpack('7i', message)
    print(data)    
    return data
    #except:
    #    print("Error in D")
def putRF(op, data): 
    if(GPIO.input(aux_pin)):                          #arguments to make function more self-contained and function-like
        length = len(data)
        length = (length & 0b00111111)
        print(length)
        end_byte = ((op << 6) | length) 
        rf_uart.write(pack('B', end_byte) + data + pack('B', end_byte))   #start byte + payload + stop byte
        rf_uart.flush() 
        return len(data)                 #waits until all data is written
    else:
        print("NOT READY")




while True:
    
    
        buf = packDEEZNUTZ()
        print("sending")
        putRF(1, buf)

'''        print("getting")
        rover_gps = getRF(8)
        if rover_gps > 0:
            rover_gps = unpackGPS(rover_gps)
            print("******************************************************************")
            print(rover_gps)
'''    
