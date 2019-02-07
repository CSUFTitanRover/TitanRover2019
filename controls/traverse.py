######################################################################################
#    Filename: traverse.py
#    Author: Chary Vielma chary.vielma@gmail.com
#    Description: Example code to use autonomousCore module
######################################################################################
# AutonomousCore module example
# insert path to python packages
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
