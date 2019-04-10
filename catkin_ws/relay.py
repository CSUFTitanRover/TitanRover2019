#!/usr/bin/env python3.5
import socket
import serial
from time import time, sleep
import socket
import struct

def unpackDEEZNUTZ(message): #object to bytes
    #try:
    data = struct.unpack('iibbbbbbbbbbbbbbbbbb', message)
    print(data)    
    return data
    #except:
    #    print("Error in D")

def putRF(data):                            #arguments to make function more self-contained and function-like
    #sleep(0.5)
    rf_uart = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_Base433_0001-if00-port0', 19200, timeout=None)
    #sleep(0.5)
    rf_uart.setDTR(True)                    #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
    rf_uart.setRTS(True)                    #then these two lines will send low logic to both which puts the module in transmit mode 0
    print("establish device")                  #Check if both send and receive buffers are empty
    rf_uart.write(b's' + data + b'f')   #start byte + payload + stop byte
    rf_uart.flush() 
    print("wrote and flushed")
    print(data)
    #sleep(0.1)
    print("putted")
    return len(data)                 #waits until all data is written
def getRF(size_of_payload): #added argument to make it more function-like
    try:
        rf_uart = serial.Serial("/dev/serial/by-id/usb-Silicon_Labs_Rover433_0001-if00-port0", 19200, timeout=0.01)
        rf_uart.setDTR(True) #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
        rf_uart.setRTS(True) #then these two lines will send low logic to both which puts the module in transmit mode 0
        while True:
            n = rf_uart.read(1) #read bytes one at a time
            print("read 1")
            if not n:
                return 0
            if n == b's': #throw away bytes until start byte is encountered
                data = rf_uart.read(size_of_payload) #read fixed number of bytes
                n = rf_uart.read(1) #the following byte should be the stop byte
                if n == b'f':
                    return data
                else: #if that last byte wasn't the stop byte then something is out of sync
                    return -1
    except:
        print("error in getRF()")
        return -1
    return -1 #should never hit this return


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
    try:
        print("receiving")
        buf = getSock()
        print(unpackDEEZNUTZ(buf))
        print("sending")
        putRF(buf)
        print(len(buf))
    
    except:
        print("error")
        sleep(0.5)
        s.close() 
        host = "192.168.1.168"
        port = 8888  # Make sure it's within the > 1024 $$ <65535 range
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        continue
