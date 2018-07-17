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

class DriveEsc:
    def __init__(self, address, mode):      # Mode can be "mixed" and "notMixed"

        # Hex Addresses For Driving Dual Motors 
        self.FORWARD_1 = 0x00
        self.REVERSE_1 = 0x01
        self.FORWARD_2 = 0x04
        self.REVERSE_2 = 0x05
        self.FORWARD_MIXED = 0x08
        self.REVERSE_MIXED = 0x09
        self.RIGHT_MIXED = 0x0A
        self.LEFT_MIXED = 0x0B
        self.RAMP = 0x10

        # To check which to operate in ("Mixed" or "NotMixed")
        if mode == "mixed":
            self.motor1 = self.FORWARD_MIXED
            self.motor2 = self.RIGHT_MIXED
        elif mode == "notMixed":
            self.motor1 = self.FORWARD_1
            self.motor2 = self.FORWARD_2

        # Serial instantiation for UART Logic
        self.port = '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0'
        self.saber = serial.Serial(self.port, '38400')
        self.address = address


    def send(self, command, message):
        # Calculate checksum termination (page 23 of the documentation).
        checksum = (self.address + command + message) & 127

        # Write data packet.
        msg = [self.address, command, message, checksum]
        msg = bytes(bytearray(msg))
        self.saber.write(msg)

        # Flush UART.
        self.saber.flush()

    def drive(self, num, speed):
        """Drive 1 or 2 motor"""
        # reverse commands are equal to forward+1
        cmds = [self.motor1, self.motor2]

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

    def driveBoth(self, speed1, speed2):
        
        if speed2 in range(-15, 15):
            self.drive(1, speed1)
            self.drive(2, speed1)
        else:
            self.drive(1, speed1)
            self.drive(2, speed2)
