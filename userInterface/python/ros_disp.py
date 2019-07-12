#!/usr/bin/env python3.5

#####################################################################################
#    Filename: ros_disp.py
#    Authors:      Timothy Parks / Chary Vielma
#    Emails:       parkstimothyj@csu.fullerton.edu / chary.vielma@csu.fullerton.edu
#    Description: ROS Dashboard - TitanRover2019
#         This program serves to display data needed to operate the robotic system
#         Output: GPS of Rover, Base, Next Coordinate
#                 Direction and Distance to Next Coordinate
######################################################################################

from tkinter import *
from tkinter import ttk
import rospy, math

############################  Testing Enable / Disable Area ##########################
test = True  #<-------------------------------------------------------test environment

# if testing disabled then live sensor data will be used
if not test:
    from finalimu.msg import fimu as imu
    from gnss.msg import gps

# if testing enabled the fake sensor data will be used
else:
    from fake_sensor_test.msg import imu
    from fake_sensor_test.msg import gps

# sets up ROS to listen for posted info
rospy.init_node('listener', anonymous=True)

# Class RosMain is the main app and the display structure
class RosMain:
    __gps = ''

    def __init__(self, master):
        # Label to Identify the UI
        self.dashlabel = ttk.Label(master, text = '\nRover Dashboard\n                                                              ')
        self.dashlabel.grid(row = 0, column = 0, columnspan = 2)

        # Label to Display the GPS
        self.gpslabel = ttk.Label(master, text = 'Location pending')
        self.gpslabel.grid(row = 1, column = 0, columnspan = 2)
        rospy.Subscriber('/gnss', gps, self.updateLabel)

        # Label to Display the Direction info
        self.dirlabel = ttk.Label(master, text = '\n\nDirection Pending')
        self.dirlabel.grid(row = 2, column = 0, columnspan = 2)
        rospy.Subscriber('/imu', imu, self.setTargetHeading)
        
        # ttk.Button(master, text = 'click me', command = self.runClick).grid(row = 1, column = 0)

    # def runClick(self):
    #     self.label.config(text = 'push me')

    # Call back function for the GPS subscriber to update the GPS label
    def updateLabel(self, data):
        '''
        Description:
            Call back for ROS call to post data from the GPS Systems
        Args:
            data - ROS topic info
        Returns:
            Nothing
        '''
        self.__gps = data
        self.gpslabel.config(text = '\nROVER GPS: \n     Latitude: ' + data.roverLat + '\n     Longitude: ' + data.roverLon + '      ' + 
                                    '\n\nBASE  GPS: \n     Latitude: ' + data.baseLat + '\n     Longitude: ' + data.baseLon + '      ' +
                                    '\n                                                              ')
    
    # Call back function for the IMU subscriber to update the Direction Label
    def setTargetHeading(self, data):
        '''
        Description:
            Code adapted from https://gist.github.com/jeromer
            Calculates and sets self.__targetHeading given self.__gps and self.$
        Args:
            None
        Returns:
            Nothing
        '''
        # if (type(self.__gps) != tuple) or (type(self.__nextWaypoint) != tuple):
        #     print("Only tuples allowed") #raise TypeError("Only tuples allowed")

        lat1 = math.radians(float(self.__gps.roverLat))
        lat2 = math.radians(float(self.__gps.destLat))

        diffLong = math.radians(float(self.__gps.destLon) - float(self.__gps.roverLon))

        x = math.sin(diffLong) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                * math.cos(lat2) * math.cos(diffLong))

        initial_heading = math.atan2(x, y)

        initial_heading = math.degrees(initial_heading)
        compassdir = (initial_heading + 360) % 360
        self.dirlabel.config(text = '\nROVER HEADING: \n     Direction: ' + str(data.yaw) + 
                                    '\n\nNEEDED HEADING:\n     Direction: ' + str(compassdir) + 
                                    '\n                                                              ')

def main():
    '''
    Description:
        Main loop to start and update app
    Args:
        None
    Returns:
        Nothing
    '''
    root = Tk()
    app = RosMain(root)
    
    # sets up event loop listener
    root.mainloop()

# Calls main
if __name__ == '__main__': main()