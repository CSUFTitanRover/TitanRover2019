#!/usr/bin/env python3.5
import socket
import serial
from time import time, sleep
import socket
import struct
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


def unpackDEEZNUTZ(message): #object to bytes
    #try:
    data = struct.unpack('iibbbbbbbbbbbbbbbbbb', message)
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




def getSock():
    try:
        s.listen(1)
        client_socket, addr = s.accept()
        while True:
            data = client_socket.recv(128)
            if data:
                return data
                break
        return data
    except:
        print("Error in getSock()")


#receive from socket, send over uart to rf module
host = "192.168.1.168"
port = 8888  # Make sure it's within the > 1024 $$ <65535 range
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 26)
s.bind((host, port))


while True:
#    try:
        print("receiving")
        buf = getSock()
        print(unpackDEEZNUTZ(buf))
        print("sending")
        putRF(buf)
        print(len(buf))
    
#    except:
#        print("error")
#        sleep(0.5)
#        s.close() 
#        host = "192.168.1.168"
#        port = 8888  # Make sure it's within the > 1024 $$ <65535 range
#        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#        s.bind((host, port))
#        continue
