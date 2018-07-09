'''
File:        pysaber.py
Author:      Rawal Shree (Github - rawalshree)
Email:       rawalshreepal000@gmail.com 
Description: PySaber class to write commands directly from TX2 / RPI  to ESC's.
             Just import the package and instantiate (create a object) the class.

             Ex. 
             from pysaber import DriveEsc
             motors = DriveEsc()
'''

import time
import serial


global FORWARD_1
global REVERSE_1
global FORWARD_2
global REVERSE_2
global FORWARD_MIXED
global REVERSE_MIXED
global RIGHT_MIXED
global LEFT_MIXED
global RAMP
global port
global saber
global address

# Hex Addresses For Driving Dual Motors 
FORWARD_1 = 0x00
REVERSE_1 = 0x01
FORWARD_2 = 0x04
REVERSE_2 = 0x05
FORWARD_MIXED = 0x08
REVERSE_MIXED = 0x09
RIGHT_MIXED = 0x0A
LEFT_MIXED = 0x0B
RAMP = 0x10

# Serial instantiation for UART Logic
port = '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0'
saber = serial.Serial(port, '38400')
address = 128

class DriveEsc:

    def send(self, command, message):
        # Calculate checksum termination (page 23 of the documentation).
        checksum = (address + command + message) & 127

        # Write data packet.
        msg = [address, command, message, checksum]
        msg = bytes(bytearray(msg))
        saber.write(msg)

        # Flush UART.
        saber.flush()

    def drive(self, num, speed):
        """Drive 1 or 2 motor"""
        # reverse commands are equal to forward+1
        cmds = [FORWARD_MIXED, RIGHT_MIXED]

        try:
            cmd = cmds[num-1]
        except:
            raise Exception('PySabertooth, invalid motor number: {}'.format(num))

        if speed < 0:
            speed = -speed
            cmd += 1

        if speed > 100:
            raise Exception('PySabertooth, invalid speed: {}'.format(speed))

        self.send(cmd, int(127*speed/100))
