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
OFF = (0, 0, 0) #light OFF
RED = (255, 0, 0) #AUX POWER
ORANGE = (255, 75, 0) #MOBILITY + ARM/SCIENCE MODULE MODE
YELLOW = (240, 255, 0) #MOBILITY ONLY MODE
GREEN = (0, 255, 0) #ALL_ON
BLUE_GREEN = (10, 255, 255) # Ebyte 433 MHZ COMM MODE
BLUE = (0, 0, 255) #Ubiquiti 3.4 GHZ COMM MODE
PURPLE = (255, 0, 127) #Attached MODULE MODE
WHITE = (255, 255, 255) #chase light

PAUSE_COLOR = RED
FULL_CONTROL = GREEN #both mobility and arm/science
MOBILITY_COLOR = BLUE #mobility only
MODULE_COLOR = PURPLE #arm/science only
MIXED_ARM = ORANGE

GHZ_COLOR = GREEN #ubiquity
MHZ_COLOR = BLUE #433 MHz backup radio

PAUSE_GHZ = 0 #red
BOTH_GHZ = 1 # green
MOBILITY_GHZ = 2 #blue
ARM_GHZ = 3 #purple
MIXED_ARM_GHZ = 4 #orange

PAUSE_MHZ = 5 #red
BOTH_MHZ = 6 # green
MOBILITY_MHZ = 7 #
ARM_MHZ = 8 #blue
MIXED_ARM_MHZ = 9 #white

#mode = 0 #value will be pulled from subscribed topic 

class Rover_Status_Lights(object):

	def __init__(self, n):
		# Create an FT232H object.
		self.ft232h = FT232H.FT232H()
		# Create a SPI interface for the FT232H object.  Set the SPI bus to 6mhz.
		self.spi    = FT232H.SPI(self.ft232h, max_speed_hz=12800000)
		# Create a pixel data buffer and lookup table.
		self.buffer = bytearray(n*24)
		self.lookup = self.build_byte_lookup()
		mode = 0






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
		for i in range(0, 7):
			self.setColor(i, r, g, b) #front right
		for i in range(53, 60):
			self.setColor(i, r, g, b) #front left
		self.show()

	def set_front_chase(self, r, g, b):
		chaseL = 53 #start status for the front left lights
		chaseR = 7 #end status for the front right lights (order is reversed between sides)
		while True:		#cycle throught the front lights from rear to front changing between blue and orange
			for i in range(7):
				self.setColor(chaseL + i, *WHITE) 
				self.setColor(chaseR - i, *WHITE)
				self.show()
				sleep(0.05)
				self.setColor(chaseL + i, r, g, b) 
				self.setColor(chaseR - i, r, g, b)
				self.show()
				sleep(0.02)
			sleep(.5)

	def set_mid(self, r, g, b):
		for i in range(7, 15):
			self.setColor(i, r, g, b) #middle front right
		for i in range(45, 53):
			self.setColor(i, r, g, b) #middle front left
		self.show()

	def set_front_half(self, r, g, b):
		for i in range(0, 15):
			self.setColor(i, r, g, b)
		for i in range(45, 60):
			self.setColor(i, r, g, b)
		self.show()

	def set_front_half_chase(self, r, g, b):
		chaseL = 45 #start status for the front left lights
		chaseR = 15 #end status for the front right lights (order is reversed between sides)
		#while True:		#cycle throught the front lights from rear to front changing between blue and orange
		for i in range(15):
			self.setColor(chaseL + i, *WHITE) 
			self.setColor(chaseR - i, *WHITE)
			self.show()
			sleep(0.03)
			self.setColor(chaseL + i, r, g, b) 
			self.setColor(chaseR - i, r, g, b)
			self.show()
			sleep(0.02)
		#sleep(.5)

	def set_rear(self, r, g, b):
		for i in range(15, 30):
			self.setColor(i, r, g, b) #rear right
		for i in range(30, 45):
			self.setColor(i, r, g, b) #rear left
		self.show()
	
	def set_all(self, r, g, b):
		for i in range(0, 60):
			self.setColor(i, r, g, b)
		self.show()


	def idle(self):
		for i in range (60):
			self.setColor(i, *WHITE)
		self.show()
		sleep(0.25)

		while True:		#cycle throught the front lights from rear to front changing between blue and orange
			chaseL = 30 #start status for the front left lights
			chaseR = 30 #end status for the front right lights (order is reversed between sides)
			for i in range(31):
				self.setColor(chaseL + i, *BLUE) 
				self.setColor(chaseR - i, *BLUE)
				self.show()
				sleep(0.03)

			sleep(.5)
			for i in range(31): 		#repeat to swap colors back
				self.setColor(chaseL + i, *ORANGE) 
				self.setColor(chaseR - i , *ORANGE)
				self.show()
				sleep(0.03)

			sleep(.5)

	def test(self):
		print("Test")
		#All directions given from behind the rover.
		for i in range(0, 59):
			self.setColor(i, *OFF) #refresh all
			self.show()
		sleep(0.25)
		for i in range(0, 7):
			self.setColor(i, *RED) #front right
		for i in range(7, 15):
			self.setColor(i, *ORANGE) #middle front right
		for i in range(15, 23):
			self.setColor(i, *YELLOW) #middle rear right
		for i in range(23, 30):
			self.setColor(i, *GREEN) #rear right sides
			
		for i in range(30, 37):
			self.setColor(i, *BLUE_GREEN) #rear left
		for i in range(37, 45):
			self.setColor(i, *BLUE) #middle rear left
		for i in range(45, 53):
			self.setColor(i, *PURPLE) #middle front left
		for i in range(53, 60):
			self.setColor(i, *WHITE) #front left
		self.show()

	def update(self, new_mode):
		self.dispatch = {
					0 : (self.set_front_half_chase, RED),
					1 : (self.set_front_half_chase, GREEN),
					2 : (self.set_front_half_chase, BLUE),
					3 : (self.set_front_half_chase, PURPLE),
					4 : (self.set_front_half_chase, ORANGE),
					5 : (self.set_front_half_chase, RED),
					6 : (self.set_front_half_chase, GREEN),
					7 : (self.set_front_half_chase, BLUE),
					8 : (self.set_front_half_chase, PURPLE),
					9 : (self.set_front_half_chase, ORANGE)
						}
		if new_mode <=4:
			self.set_rear(*GREEN)
		else:
			self.set_rear(*BLUE)
		self.dispatch[new_mode][0](*self.dispatch[new_mode][1])




