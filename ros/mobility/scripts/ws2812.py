'''
Author: Georden Grabuskie ggrabuskie@csu.fullerton.edu
Driving ws2812 LED light strip from an SPI bus.

This code operates by syncing sent data to match the expected input
timing of the ws2812 LED light strips.
Uses the FT232H breakout board to add SPI capability to an open
USB port.

All base code taken directly from 
https://learn.adafruit.com/adafruit-ft232h-breakout/spi
'''

from time import sleep
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.FT232H as FT232H

#tuples to be used as operands

#COLORS
OFF = (0, 0, 0) #light OFF
RED = (255, 0, 0) #AUX POWER
ORANGE = (255, 75, 0) #MOBILITY + ARM/SCIENCE MODULE MODE
YELLOW = (240, 255, 0) #MOBILITY ONLY MODE
GREEN = (0, 255, 0) #ALL_ON
BLUE_GREEN = (10, 255, 255) # Ebyte 433 MHZ COMM MODE
BLUE = (0, 0, 255) #Ubiquiti 3.4 GHZ COMM MODE
PURPLE = (255, 0, 127) #Attached MODULE MODE
WHITE = (255, 255, 255) #chase light
PINK = (255, 20, 147)

#MODE = COLOR
PAUSE = RED #L2 + R2
IDLE = 0
MOBILITY = YELLOW #R2 + L1
ARM = BLUE_GREEN    #R2 + 3
BOTH = ORANGE # R2 + 1

#COMMS = COLOR
LOCAL_COLOR = BLUE #any controller plugged into the rover
GHZ_COLOR = GREEN #ubiquity
MHZ_COLOR = PURPLE #433 MHz backup radio
APP_COLOR = BLUE_GREEN


class Rover_Status_Lights(object):

	def __init__(self, n):
		# Create an FT232H object.
		self.ft232h = FT232H.FT232H()
		# Create a SPI interface for the FT232H object.  Set the SPI bus to 6mhz.
		self.spi    = FT232H.SPI(self.ft232h, max_speed_hz=12800000)
		# Create a pixel data buffer and lookup table.
		self.buffer = bytearray(n*24)
		self.lookup = self.build_byte_lookup()

	def build_byte_lookup(self):
		# Create a lookup table to map all byte values to 8 byte values which
		# represent the 6mhz SPI data to generate the NeoPixel signal for the
		# specified byte.
		lookup = {}
		for i in range(256):
			value = bytearray()
			for j in range(7, -1, -1):
				if ((i >> j) & 1) == 0:
					value.append(0b11100000)
				else:
					value.append(0b11111000)
			lookup[i] = value
		return lookup

	def setColor(self, n, r, g, b):
		# Set the pixel RGB color for the pixel at position n.
		# Assumes GRB NeoPixel color ordering, but it's easy to change below.
		index = n*24
		self.buffer[index   :index+8 ] = self.lookup[int(g)]
		self.buffer[index+8 :index+16] = self.lookup[int(r)]
		self.buffer[index+16:index+24] = self.lookup[int(b)]

	def show(self):
		# Send the pixel buffer out the SPI data output pin (D1) as a NeoPixel
		# signal.
		self.spi.write(self.buffer)

	def set_front(self, r, g, b):
		chaseL = 46 #start status for the front left lights
		chaseR = 15 #end status for the front right lights (order is reversed between sides)
		for i in range(15):
			self.setColor(chaseL + i, *WHITE) 
			self.setColor(chaseR - i, *WHITE)
			self.show()
			sleep(0.03)
			self.setColor(chaseL + i, r, g, b) 
			self.setColor(chaseR - i, r, g, b)
			self.show()
			sleep(0.02)

	def set_rear(self, r, g, b):
		#chaseL = 31 #start status for the front left lights
		#chaseR = 30 #end status for the front right lights (order is reversed between sides)
		for i in range(15, 45):
			'''
			self.setColor(chaseL + i, *WHITE) 
			self.setColor(chaseR - i, *WHITE)
			self.show()
			sleep(0.03)
			self.setColor(chaseL + i, r, g, b) 
			self.setColor(chaseR - i, r, g, b)
			'''
			self.setColor(i, r, g, b)
			self.show()
			#sleep(0.02)

	def set_all(self, r, g, b):
		chaseL = 31 #start status for the front left lights
		chaseR = 30 #end status for the front right lights (order is reversed between sides)
		for i in range(30):
			self.setColor(chaseL + i, *WHITE) 
			self.setColor(chaseR - i, *WHITE)
			self.show()
			sleep(0.03)
			self.setColor(chaseL + i, r, g, b) 
			self.setColor(chaseR - i, r, g, b)
			self.show()
			sleep(0.02)

	def idle(self, r, g, b):
		for k in range(5):
			chaseL = 30
			chaseR = 29
			for j in range(60):
				self.setColor(j, *BLUE)
			for i in range (k, 30, 5):
				self.setColor(chaseL + i, *ORANGE)
				self.setColor(chaseR - i, *ORANGE)
			self.show()
			sleep(0.5)

	def update(self, new_mode, new_source):
		self.dispatch = {
					-1 : (self.set_front, PAUSE),
					0 : (self.idle, WHITE), #argument used to match parameters for other functions in dictionary
					1 : (self.set_front, MOBILITY),
					2 : (self.set_front, ARM),
					3 : (self.set_front, BOTH),
						}
		self.comms = {
					0 : (self.set_rear, LOCAL_COLOR),
					1 : (self.set_rear, GHZ_COLOR),
					2 : (self.set_rear, MHZ_COLOR),
					3 : (self.set_rear, PINK)
					}
		self.comms[new_source][0](*self.comms[new_source][1])
		self.dispatch[new_mode][0](*self.dispatch[new_mode][1])




