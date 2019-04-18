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
points = [(33.88409, -117.88451),
(33.88409, -117.88455),
(33.88409, -117.88459),
(33.88411, -117.88462),
(33.88412, -117.88466),
(33.88412, -117.8847),
(33.88413, -117.88474),
(33.88414, -117.88478),
(33.88414, -117.88482),
(33.88415, -117.88486),
(33.88415, -117.8849),
(33.88411, -117.88514),
(33.88412, -117.88521),
(33.88415, -117.88525),
(33.88415, -117.88529),
(33.88415, -117.88533),
(33.88414, -117.88529),
(33.88416, -117.88532),
(33.88423, -117.88533),
(33.88427, -117.8853),
(33.88433, -117.88519),
(33.88433, -117.88524),
(33.88439, -117.88525),
(33.88441, -117.88522),
(33.88442, -117.88518),
(33.88441, -117.88514),
(33.88441, -117.8851),
(33.8844, -117.88506),
(33.88439, -117.88502),
(33.88436, -117.88498),
(33.88435, -117.88494),
(33.88432, -117.88491),
(33.8843, -117.88487),
(33.88427, -117.88484),
(33.88425, -117.88481),
(33.88423, -117.88478),
(33.88421, -117.88475),
(33.88418, -117.88472),
(33.88416, -117.88469),
(33.88414, -117.88466),
(33.88413, -117.88462),
(33.88415, -117.88459),
(33.88414, -117.88455),
(33.88414, -117.88451),
(33.88413, -117.88443),
(33.88414, -117.88447) ] #(33.884165, -117.884901), (33.884304, -117.884676), (33.884091, -117.884475)]

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
