#!/usr/bin/env python3.5
import socket
import serial
from time import time, sleep
import socket
from struct import pack, unpack
import RPi.GPIO as GPIO
MOBILITY_OP = 0b00
GPS_OP = 0b01
TERMINAL_OP = 0b10

GPIO.setmode(GPIO.BCM)
mode_pin = [23, 24]
aux_pin = 18

for pin in mode_pin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
GPIO.setup(aux_pin, GPIO.IN)

rf_uart = serial.Serial('/dev/ttyAMA0', 19200, timeout=1.0)
GPIO.output(mode_pin[0], 0)                    #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
GPIO.output(mode_pin[1], 0)                    #then these two lines will send low logic to both which puts the module in transmit mode 0



'''
FUNCTION: putRF
ARGS:
    OPCODE = 2 bits 0b00-0b11 represents purpose/mode of message
    DATA = data payload packed using struct.pack
RETURNS: none
'''
def putRF(op, data = b''): 
    if(GPIO.input(aux_pin)):                          #arguments to make function more self-contained and function-like
        length = len(data)
        length = (length & 0b00111111)
        print(length)
        end_byte = ((op << 6) | length)
        if length > 0:
            rf_uart.write(pack('B', end_byte) + data + pack('B', end_byte))   #start byte + payload + stop byte
            rf_uart.flush() 
            return len(data)                 #waits until all data is written
        else:
            rf_uart.write(pack('B', end_byte) + pack('B', end_byte))   #start byte + payload + stop byte
            rf_uart.flush() 
            return 0                #waits until all data is written

    else:
        print("NOT READY")

'''
FUNCTION: getRF
ARGS: none
RETURNS: 
    OPCODE = 2 bits 0b00-0b11 represents purpose/mode of message
    DATA = data payload packed using struct.pack
'''
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
            if length > 0:
                data = rf_uart.read(length) 
                stop_byte = unpack('B', rf_uart.read(1))[0] #the following byte should be the stop byte
                if start_byte == stop_byte:
                    print("ENDS MATCH")
                    print(op)
                    print(data)
                    return (op, data)
                else: #if that last byte wasn't the stop byte then something is out of sync
                    print("BAD ENDS")
                    return (-1, -1)
            else:
                return (op, 0)


'''   1 import socket
   2 
   3 UDP_IP = "127.0.0.1"
   4 UDP_PORT = 5005
   5 
   6 sock = socket.socket(socket.AF_INET, # Internet
   7                      socket.SOCK_DGRAM) # UDP
   8 sock.bind((UDP_IP, UDP_PORT))
   9 
  10 while True:
  11     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  12     print "received message:", data
'''
def getSock():
    try:
        while True:
            data, addr = s.recvfrom(128) # buffer size is 1024 bytes
            if data:
                return data
    except Exception as e:
        print("Error in getSock()")
        print(e)

def request_gps():
    try:
        putRF(GPS_OP) #send just the GPS request OP to rover,
        # empty data arg defaults to empty string and the function
        #  will only send the end bytes
        unused_op, packed_gps = getRF() #gets op code and data returned, data returned will be a packed
        #struct containing two floats for lat, lon
        location = unpack('2f', packed_gps)
        return location #location is a tuple
    except Exception as e:
        print(e)



#receive from socket, send over uart to rf module
host = "192.168.1.168"
port = 8888  # Make sure it's within the > 1024 $$ <65535 range
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 26)
s.settimeout(5.0) #set timeout to 10 seconds if no data is received over the
#socket in 10 seconds then socket times out and request gps
s.bind((host, port))


while True:
#    try:
        print("receiving")
        buf = getSock() #get mobility command from socket (from multijoy)
        if buf: #if data received without timeout
            print(unpack('2i18b', buf))
            print("sending")
            putRF(0b00, buf) #send op code 00 for mobility and the data received
            print(len(buf))
        else: #if timeout send op_code 0b01 requesting gps then listen for response
            location = request_gps()
            print (location)

    
