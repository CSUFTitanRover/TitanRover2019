######################################################################################
#    Filename: traverse.py
#    Authors:      Chary Vielma / Shripal Rawal
#    Emails:       chary.vielma@csu.fullerton.edu / rawalshreepal000@gmail.com
#    Description: Example code to use autonomousCore module
######################################################################################
# AutonomousCore module example

import sys
import subprocess

rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from driver import Driver
myDriver = Driver()

# List with CSUF test coordinates
points = [(33.88239, -117.883568)] #, (33.88239 , -117.883568), (33.882513, -117.88.607751), (33.882434, -117.8835028), (33.88245 , -117.883660)]

# Drives to each point in a list
for point in points:
    myDriver.goTo(point)

# Rotates Rover to face given heading
#myDriver.rotateToHeading(315)

# Set min/max forward speeds
#myDriver.setMinMaxFwdSpeeds(35, 45)

# Calculate GPS point based on current GPS coordinate, heading and Distance
#crd = (33.882727498, -117.883965627)
#heading = 0
#distance = 100
#point = myDriver.calcuateGps(crd, heading, distance)

# Calculate the spiral points to travel
#radius = 400        # 400 Cm --> 4 Mt
#spilist = myDriver.spiralPoints(pt, radius)

# Travel all the points in the spilist(In Concentric Circles)
#while len(spilist) > 0:
    #myDriver.goTo(spilist[-1])
    #spilist.pop()
