#!/usr/bin/env python3.5
import socket, serial
from time import time, sleep
from struct import pack, unpack
rf_uart = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_Rover433_0001-if00-port0', 19200, timeout=10)
rf_uart.setDTR(True) #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
rf_uart.setRTS(True) #then these two lines will send low logic to both which puts the module in transmit mod$


def unpackDEEZNUTZ(message): #object to bytes
#    try:
        data = unpack('7i', message)
        return data
#    except:
#        print("Error in D")
#        return 0

def packGPS():
    return pack("2i", int(1234), int(5678))


def getRF():
        op = 0b00
        length = 0b000000
        start_byte = 0
        start_byte = unpack('B', rf_uart.read(1))[0] #wait for byte until timeout
        if start_byte == 0:
            return 0 #if timeout return 0
        else:
            op = (start_byte >> 6)
            print("OP")
            print(op)
            length = (start_byte & 0b00111111)
            print("LENGTH")
            print(length)
            data = rf_uart.read(length) 
            stop_byte = unpack('B', rf_uart.read(1))[0] #the following byte should be the stop byte
            if start_byte == stop_byte:
                print("ENDS MATCH")
                print(op)
                print(data)
                return (op, data)
            else: #if that last byte wasn't the stop byte then something is out of sync
                print("BAD ENDS")
                return -1    


gps_flag = True
while True:
    data = getRF()
    if data > 1:
        print("data good?")
        print(unpack('7i', data[1]))
'''
        print("receiving")
        buf = getRF(28)
        print(buf)
        if buf > 0:
            buf = unpackDEEZNUTZ(buf)
        print(buf)
        if ((int(time()) % 10 ) < 5) and gps_flag:
            print("sending**********************************************************************")
            putRF(packGPS())
            gps_flag = False
        elif ((int(time()) % 10) > 5):
            gps_flag = True
'''  
