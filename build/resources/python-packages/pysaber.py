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
import serial, os

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
        x = os.system('ls /dev/serial/by-id/usb-Silicon_Labs_RoverESC_0001-if00-port0')
        if x == 0:
            self.port = '/dev/serial/by-id/usb-Silicon_Labs_RoverESC_0001-if00-port0'
            print('ESC Rover')
        else:
            self.port = '/dev/serial/by-id/usb-Silicon_Labs_RoverUART_0001-if00-port0'
            print('ESC Runt')
        self.saber = serial.Serial(self.port, '38400')
        self.address = address

        self.send(0x0E, 6)          # To set Timeout
        self.send(0x0F, 4)          # To set Baudrate


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
            speed = 100
            #raise Exception('PySabertooth, invalid speed: {}'.format(speed))

        self.send(cmd, int(127*speed/100))

    def driveBoth(self, speed1, speed2):
        if speed1 != 0 and speed2 in range(-10, 10):
            self.drive(1, speed1)
            self.drive(2, 0)
        else:
            self.drive(1, speed1)
            self.drive(2, speed2)
