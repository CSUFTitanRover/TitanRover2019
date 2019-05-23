#!/usr/bin/env python

'''
File:         mhzRx.py
Authors:      Georden Grabuskie / Shripal Rawal / Timothy Parks 
Emails:        ggrabuskie@csu.fullerton.edu / rawalshreepal000@gmail.com / parkstimothyj@gmail.com 
Description:  Listens to Ebyte E32 transceiver and publishes telecommands to ROS
'''

import rospy, serial
from multijoy.msg import MultiJoy
from sensor_msgs.msg import Joy
from mobility.msg import Status
from struct import pack, unpack
from time import sleep, time
rf_uart = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_Rover433_0001-if00-port0', 19200, timeout=None)
rf_uart.setDTR(True) #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
rf_uart.setRTS(True) #then these two lines will send low logic to both which puts the module in transmit mod$

'''
FUNCTION: putRF
ARGS:
    OPCODE = 2 bits 0b00-0b11 represents purpose/mode of message
    DATA = data payload packed using struct.pack
RETURNS: none
'''
def putRF(op, data): 
    print(rf_uart.cts)
    length = len(data)
    length = (length & 0b00111111)
    print(length)
    end_byte = ((op << 6) | length) 
    rf_uart.write(pack('B', end_byte) + data + pack('B', end_byte))   #start byte + payload + stop byte
    rf_uart.flush() 
    print("sent")
    return len(data)                 #waits until all data is written

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
        buf = rf_uart.read(1)
        if buf:
            start_byte = unpack('B', buf)[0] #wait for byte until timeout
        if start_byte == 0:
            return (-1, -1) #if timeout return 0
        else:
            op = (start_byte >> 6)
            print("OP")
            print(op)
            length = (start_byte & 0b00111111)
            print("LENGTH")
            print(length)
            #if length > 0:
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
            #else:
            #    return (op, 0)

'''
FUNCTION: mobility_action
ARGS:
    MESSAGE = data payload returned from getRF packed using struct.pack
RETURNS: none
DESCRIPTION: Unpacks message expecting a mobility command. It will extract
the mobility data into the appropriate object then publish it to ROS. If the 
data is not as expected an error will be thrown by the assignment because of a
type mismatch or by ROS because of formatting that doesn't match the message type.
'''
def mobility_action(message): #object to bytes
    try:
        data = unpack('2i18b', message)
        print(time())
        print(data[0])
        if int(time()) != data[0]:
            print("STALE COMMAND")
            return
        global multijoy_pub
        msg = MultiJoy()
        msg.source = 2
        msg.njoys.data = 1
        t_joy = Joy()
        t_joy.header.stamp.secs = data[0]
        t_joy.header.stamp.nsecs = data[1]
        for i in range(2, 8):
            t_joy.axes.append(float(float(data[i]) / float(127)))
        for i in range(8, 20):
            t_joy.buttons.append(data[i])
        
        msg.joys.append(t_joy)
        multijoy_pub.publish(msg)
        print(msg)
        print("PUBLISHED")
    except:
        print("Error in D")

def send_gps(data):
    print("gonna send gps")
    gps = pack("2f", float(123.4), float(567.8))
    putRF(0b01, gps)

def error_happened(data):
    print("Error Happened")
    print("Data:")
    print(data)
'''
FUNCTION: update
ARGS:
    OPCODE = 2 bits 0b00-0b11 represents purpose/mode of message
    MESSAGE = data payload returned from getRF packed using struct.pack
RETURNS: none
DESCRIPTION: checks op_code and calls the appropriate function.
'''
def update(op_code, message):
    dispatch = {
                -1 : error_happened,
                0 : mobility_action, #Mobility command
                1 : send_gps, #request for GPS
                    }
    dispatch[op_code](message)


def monitor():
    while not rospy.is_shutdown():
        try:
            print(rf_uart.cts)
            op_code, message = getRF()
            print("OP: " + str(op_code))
            print("Message: " + str(message))
            update(op_code, message)
        except Exception as e: 
            print(e)
            print("Error in main loop")

if __name__ == '__main__':
    try:
        rospy.init_node('MHz_Publisher', anonymous=True)
        multijoy_pub=rospy.Publisher('/multijoy', MultiJoy, queue_size=1)   #publisher for multijoy

        monitor()
    except rospy.ROSInterruptException:
        quit()