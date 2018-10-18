'''
Author: Georden Grabuskie ggrabuskie@csu.fullerton.edu
Driving ws2812 LED light strip from an SPI bus.

This code operates by syncing sent data to match the expected input
timing of the ws2812 LED light strips.
Uses the FT232H breakout board to add SPI capability using an open
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

# mode 0 = both, mode 1 = mobility, mode 2 = arm, mode 3 = arm Single(Not Mixed)
AUX_COLOR = RED #auxillary power
ALL_COLOR = GREEN #auxillary and main power
MOBILITY_COLOR = YELLOW #mobility only
MODULE_COLOR = PURPLE #arm/science only
FULL_CONTROL = ORANGE #both mobility and arm/science
GHZ_COLOR = BLUE #ubiquity
MHZ_COLOR = BLUE_GREEN #433 MHz backup radio

PAUSE = 0 #red
BOTH = 1 # purple
MOBILITY = 2 #green
ARM = 3 #blue
MIXED_ARM = 4 #white
mode = 0 #value will be pulled from subscribed topic 

class Rover_Status_Lights():

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
		print(r + g + b)
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

	def set_rear(self, r, g, b):
		for i in range(15, 30):
			self.setColor(i, *BLUE) #rear right
		for i in range(30, 45):
			self.setColor(i, *ORANGE) #rear left
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

	def update(self, mode):

		self.dispatch = {
					0 : (self.set_all, RED),
					1 : (self.set_all, PURPLE),
					2 : (self.set_all, GREEN),
					3 : (self.set_all, BLUE),
					4 : (self.set_all, BLUE_GREEN)
					#0 : (self.set_front_chase, FULL_CONTROL),
					#1 : (self.set_front_chase, MOBILITY_COLOR),
					#2 : (self.set_front_chase, MODULE_COLOR),
					#"aux" : (self.set_mid, AUX_COLOR),
					#"all" : (self.set_mid, ALL_COLOR),
					#"ghz" : (self.set_rear, GHZ_COLOR),
					#"mhz" : (self.set_rear, MHZ_COLOR)
						}

		self.dispatch[mode][0](*self.dispatch[mode][1])




# Run this code when the script is called at the command line:
#if __name__ == '__main__':
	# Define the number of self in the NeoPixel strip.
	# Only up to ~340 self can be written using the FT232H.
	#pixel_count = 60
	# Create a NeoPixel_FT232H object.
	#status = Rover_Status_Lights(pixel_count)
	#status.set_all(*OFF)
	#status.update(mode)
	#status.test()
	#status.set_front_chase(*RED)

