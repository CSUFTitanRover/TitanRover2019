'''
File:        pysaber.py
Author:      Rawal Shree (Github - rawalshree)
Email:       rawalshreepal000@gmail.com 
Description: Class to write use GPIO directly to TX2 / RPI  I/O pins.
             Just import the package and instantiate (create a object) the class.

             Ex. 
             from pysaber import DriveEsc
             motors = DriveEsc()
'''

from sysfs.gpio import Controller, OUTPUT, INPUT

class Tx2Gpio:
    def __init__(self, pins):
        
        # Allocates the pins to be used as GPIO
        Controller.available_pins = pins

    def setup(self, Pin, Mode):
        if Mode == 'out':
            Controller.alloc_pin(Pin, OUTPUT)
        elif Mode == 'in':
            Controller.alloc_pin(Pin, INPUT)

    def output(self, pin, value):
        if value == 1:
            Controller.set_pin(pin)
        else:
            Controller.reset_pin(pin)

    def read(self, pin):
        pin = Controller.alloc_pin(1, INPUT)
        return pin.read()