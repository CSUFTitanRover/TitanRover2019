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
points = [(33.882292,-117.884238), (33.881974,-117.883981), (33.882292,-117.884238)] #(33.882554, -117.883785)] #, (33.882641, -117.883943)]
# (33.882554, -117.883688), (33.882440, -117.883611), (33.882110, -117.883634), (33.881974, -117.883878), (33.881909, -117.884134), (33.881984, -117.884443), (33.882065, -117.884493), (33.882223, -117.884577), (33.882492, -117.884436), (33.882638, -117.884322), (33.882654, -117.884100), (33.882641, -117.883943)]

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
