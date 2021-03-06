#!/usr/bin/env python

#Timothy Parks mock slam design
# 2d array 3281 x 3281 ft
# 2d array 1000 x 1000 m
# precision to 0.00001 about 1m

import sys , subprocess, threading, rospy
import random, time, math, re
import numpy as np
# To import packages from different Directories
rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from roverdb import Database
from astar import astar

test = True  #<-----------------------------------------------------------------------------test environment
debug = True

if not test:
    from finalimu.msg import fimu as imu
    from mode.msg import mode as mode
    from gnss.msg import gps

else:
    from fake_sensor_test.msg import imu
    from fake_sensor_test.msg import gps

## Global Variables
measurement_array = []
#current_start_pos_gps = {'lat':0 ,'lon': 0}  #(Latitude, Longitude)

class slam():
    
    #from driver import Driver as myDriver
    #from gnss.msg import gps as msg
    

    global measurement_array, test
    _dimx = 0
    _dimy = 0
    _precision = 0
    _boarder = 0.00009 # padded edge for map
    _acceleration = 0
    _mode_info = 0
    _heading = 0
    fill_val = np.int8(-1)
    #myDriver = Driver()
    db = Database()
    slam_map = []
    slam_map_list_type = []
    scan = []
    current_pos_gps = {'lat':0 ,'lon': 0}  #(Latitude, Longitude)
    org_offset_gps  = {'lat':0 ,'lon': 0}
    dest_gps        = {'lat':0 ,'lon': 0}
    #augments the gps after 5 decimal cut
    curr_dir = 0
    
    


    ###################################################################################
    ######## Start the slam object this specific settings
    def __init__(self, dimx, dimy, precision): #, current_lat, current_lon):
        self._dimx = dimx
        self._dimy = dimy
        self._precision = precision #should be 0.00001
        self.current_pos_gps['lat'] = 0
        self.current_pos_gps['lon'] = 0
        self.update_sensors()
        ## GPS Array Creation
        self.fillMap()  # Array of default size populated with fill_val  
        self.update_sensors()
        print('before org offsetS')
        ## Grid Offset start location latitude
        if self.current_pos_gps['lat'] > 0:
            self.org_offset_gps['lat'] = self.truncate(self.current_pos_gps['lat'],5) + (((self._dimx - 1.0)/2.0) * self._precision) #float(format(current_lat + ((self._dimx - 1)/2) * self._precision,'.5f')) 
        else:
            self.org_offset_gps['lat'] = self.truncate(self.current_pos_gps['lat'],5) - (((self._dimx - 1.0)/2.0) * self._precision)  #float(format(current_lat - ((self._dimx - 1)/2) * self._precision,'.5f')) 

        ## Grid Offset start location longitude
        self.org_offset_gps['lon'] = self.truncate(self.current_pos_gps['lon'],5) - (((self._dimy - 1.0)/2.0) * self._precision)  #float(format(current_lon - ((self._dimy - 1)/2) * self._precision,'.5f')) 

        #ROS startup functions
        rospy.init_node('listener', anonymous=True)
        ##############################rospy.init_node('listener', anonymous=True)
        # auto_sensors = threading.Thread(target=update_sensors)
        # auto_sensors.start()

    ###################################################################################
    ######## numpy made readible
    def fillMap(self):
        self.slam_map = np.full((self._dimy, self._dimx), self.fill_val, dtype=np.int8)
        '''
        dimx = dimy = 3
        example output for np.full((dimy, dimx), -1, dtype=np.int8)
           [[-1. -1. -1.]
            [-1. -1. -1.]
            [-1. -1. -1.]] FYI the dimx and dimy are switched in function call 
        '''

    def append_y(self):
        self.slam_map = np.insert(self.slam_map, self._dimy, self.fill_val, axis=0)
        self._dimy += 1
        '''
        example output for: print(slamit.slam_map); slamit.fill_val = 2; slamit.append_x(); print(slamit.slam_map)
           [[-1 -1 -1] before
            [-1 -1 -1]
            [-1 -1 -1]]
           [[-1 -1 -1] after
            [-1 -1 -1]
            [-1 -1 -1]
            [ 2  2  2]]
        '''

    def append_x(self):
        self.slam_map = np.insert(self.slam_map, self._dimx, self.fill_val, axis=1)
        self._dimx += 1
        '''
        example output for: print(slamit.slam_map); slamit.fill_val = 2; slamit.append_x(); print(slamit.slam_map)
           [[-1 -1 -1] before
            [-1 -1 -1]
            [-1 -1 -1]]
           [[-1 -1 -1  2]  after
            [-1 -1 -1  2]
            [-1 -1 -1  2]]
        '''

    def insert_x(self):
        self.org_offset_gps['lon'] = (math.floor((self.org_offset_gps['lon'] - self._precision) * 10 ** 5)) / 10 ** 5
        self.slam_map = np.insert(self.slam_map, 0, self.fill_val, axis=1)
        self._dimx += 1
        '''
        example output for: print(slamit.slam_map); slamit.fill_val = 2; slamit.insert_x(); print(slamit.slam_map)
           [[-1 -1 -1] before
            [-1 -1 -1]
            [-1 -1 -1]]
           [[ 2 -1 -1 -1]  after
            [ 2 -1 -1 -1]
            [ 2 -1 -1 -1]]
        '''

    def insert_y(self):
        self.org_offset_gps['lat'] = (math.floor((self.org_offset_gps['lat'] + self._precision) * 10 ** 5)) / 10 ** 5
        temp_arr = np.full((1, self._dimx), self.fill_val, dtype=np.int8)
        self.slam_map = np.insert(temp_arr, 1, self.slam_map, axis=0)
        self._dimy += 1
        '''
        example output for: print(slamit.slam_map); slamit.fill_val = 2; slamit.insert_y(); print(slamit.slam_map)
           [[-1 -1 -1]  before
            [-1 -1 -1]
            [-1 -1 -1]]
           [[ 2  2  2]  after
            [-1 -1 -1]
            [-1 -1 -1]
            [-1 -1 -1]]
        '''
    def expand_map(self):
        import sqlite3
        logindbfile = 'rover.sqlite3'
        conn = sqlite3.connect(logindbfile)
        cur = conn.cursor()
        num_coords = self.db.getTableSize('map')
        for x in range(num_coords):
            newpoints = self.db.getLatLonValue(x + 1)  
            sql_lat, sql_lon =  float(newpoints[0]), float(newpoints[1])
            newgps = self.gps_trunc(sql_lat, sql_lon)
            print(newpoints)
            
            # widen the y_plane
            if (newgps[0] - self._boarder) < (self.org_offset_gps['lat'] - (self._dimy * self._precision)):
                print('in first y appending ' + str(int(math.floor((newgps[0] - (self.org_offset_gps['lat'] -  (self._dimy * self._precision + self._boarder))) * 10 ** 5))))
                for i in range(int(math.floor(abs((newgps[0] - (self.org_offset_gps['lat'] -  (self._dimy * self._precision + self._boarder)))) * 10 ** 5))):
                    self.append_y() #append difference amount
            
            if (newgps[0] + self._boarder) > self.org_offset_gps['lat']:
                print('in second y inserting ' + str(int(math.floor((newgps[0] + self._boarder - self.org_offset_gps['lat'])* 10 ** 5))) + '\n')
                for i in range(int(math.floor(abs(((newgps[0] + self._boarder - self.org_offset_gps['lat'])))* 10 ** 5))):
                    self.insert_y() #insert difference amount

            # widen the x-plane
            if (newgps[1] + self._boarder) > (self.org_offset_gps['lon'] + (self._dimx * self._precision)):
                print('in first x appending ' + str(int(math.floor(((newgps[1] + self._boarder) - (self.org_offset_gps['lon'] + (self._dimx * self._precision))) * 10 ** 5))))
                for i in range(int(math.floor(abs(((newgps[1] + self._boarder) - (self.org_offset_gps['lon'] + (self._dimx * self._precision)))) * 10 ** 5))):
                    self.append_x() #append difference amount
            
            if (newgps[1] - self._boarder) < self.org_offset_gps['lon']:
                print('in second x inserting ' + str(int(math.floor((self.org_offset_gps['lon'] - (newgps[1] - self._boarder)) * 10 ** 5))) + '\n')
                for i in range(int(math.floor(abs((self.org_offset_gps['lon'] - (newgps[1] - self._boarder))) * 10 ** 5))):
                    self.insert_x() #insert difference amount

    ######################################################################################
    ####### create list version of map
    def listIt(self):
        self.slam_map_list_type = self.slam_map.tolist()

    ######################################################################################
    ####### math Truncating to 5 decimal positions without rounding
    def truncate(self, f, n):
        return math.floor(f * 10 ** n) / 10 ** n

    ######################################################################################
    ####### math Truncating to 5 decimal positions without rounding a tuple design for gps
    def gps_trunc(self, f_lat, f_lon):
        import math
        return math.floor(f_lat * 10 ** 5)/(10 ** 5) , math.floor(f_lon * 10 ** 5)/(10 ** 5)

    ######################################################################################
    ####### setDistance for distance measurements between 2 GPS points
    def setDistance(self):
        global __nextWaypoint, __gps, __distance
        '''
        Description:
            Haversine formula - Calculates and sets self.__distance (in cm) given self.__gps 
            and self.__nextWaypoint
        Args:
            None
        Returns:
            Nothing
        '''
        a1, b1 = __gps
        a2, b2 = __nextWaypoint
        radius = 6371 # km

        da = math.radians(a2-a1)
        dc = math.radians(b2-b1)
        a = math.sin(da/2) * math.sin(da/2) + math.cos(math.radians(a1)) \
            * math.cos(math.radians(a2)) * math.sin(dc/2) * math.sin(dc/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c
        __distance = d * 100000

    #Other 2D array design
    # gps_arr = [[0 for x in range(1000)] for y in range(1000)] 
    ######################################################################################
    ####### LiDAR Update
    def scan_update(self):
        #scan, curr_dir, measurement_array
        pass
        
    def update_sensors(self):
        if not test:
            
            rospy.Subscriber('/mode', mobility, self.update_mode)
            rospy.Subscriber('/imu', fimu, self.update_acceleration)
            rospy.Subscriber('/gnss', gps, self.update_gnss)
            rospy.Subscriber('/ce30', ce30, self.update_lidar)
        else:
            rospy.Subscriber('/imu', imu, self.update_acceleration)
            rospy.Subscriber('/gnss', gps, self.update_gnss)
        
    def update_lidar(self):
        pass
    
    def update_acceleration(self, data):
        global test
        if not test:
            self._acceleration = float(data.yaw.pitch)
            self._heading = float(data.yaw.yaw)
        else:
            self._acceleration = float(data.pitch)
            self._heading = float(data.yaw)

    def update_mode(self, data):
        self._mode_info = data.data

    def update_gnss(self, data):
        self.current_pos_gps['lat'] = float(data.roverLat)
        self.current_pos_gps['lon'] = float(data.roverLon)    


#######################################################################################
def start_init():
    pass

######################################################################################
##  Contour Map setup
def make_map_image(dimx, dimy):
    from PIL import Image
    img = Image.new('RGB', (dimx,dimy), 'black')
    pixels = img.load()

    ##  Contour Map coloring ranges
    colors = {'-1':(211,211,211), '1':(255,255,255),'2':(255,204,204),'3':(255,153,153),
                '4':(255,102,102),'5':(255,51,51),'6':(255,0,0),'7':(204,0,0),'8':(153,0,0),
                '9':(102,0,0),'10':(51,0,0), '11':(0,0,0)}
    
    #img.show()
    #img.save('rover_map','png')
    #print('image written')

# def update_gnss(data):
#     from math import floor
#     global current_start_pos_gps
#     current_start_pos_gps = floor(float(data.roverLat) * 10 ** 5)/(10 ** 5) , floor(float(data.roverLon) * 10 ** 5)/(10 ** 5)

    #current_start_pos_gps['lat'] = float(data.roverLat)
    #current_start_pos_gps['lon'] = float(data.roverLon)

def main():
    # global current_start_pos_gps
    ## test points to prepare array
    #current_lon = -117.882759 # horizontal Fullerton E21 Backdoor
    #current_lat = 33.881825  #vertical Fullerton E21 Backdoor
    start_init() #prep work for start
    
    # dim's must be odd number size and form square for initialization 
    slamit = slam(3, 3, 0.00001) #, current_start_pos_gps['lat'], current_start_pos_gps['lon']) #   current_lat, current_lon)
    slamit.update_sensors()
    print(slamit.slam_map)
    print(slamit.current_pos_gps)
    print(slamit.org_offset_gps)
    #slamit.scan = measurement_array
    slamit.fill_val = 0
    slamit.curr_dir = 45 
    slamit.expand_map()
    print(slamit.slam_map)
    print(slamit._dimx, slamit._dimy)
    print(slamit.org_offset_gps)
    print(slamit.org_offset_gps['lat']-(slamit._dimy * slamit._precision), slamit.org_offset_gps['lon'] + (slamit._dimx * slamit._precision))
    # start = (0,0)
    # end = (2, 10)
    # maze = slamit.slam_map.tolist()
    # print(astar(maze, start, end))
    '''
    while:
        next point in driver.goto() 
        if next point type ==  scoutprimary
            call varun function
        if next point type == primary
            call varun
            call spiral
            add list to db
        if next point type == spiral
            goto point
            call varun
        if next point type == ball
            goto point
            call ballmotherfucker
                wait 10sec
                display ball
            clear all spiral
            
            


    '''

    #print(distance(current_pos_gps, dest_gps).cm)

if __name__ == '__main__':
    #need ros spin?
    main()



    # try:
    #     rospy.init_node('talker_scan', anonymous=True)
    #     msg = joystick()
    #     rospy.Subscriber('lidar', lidar, main)
    #     rospy.spin() 
    # except(KeyboardInterrupt, SystemExit):
    #     rospy.signal_shutdown()
    #     raise



###################################################################################
##### Another Python Array Implementation

## prepopulated with GPS points based on start as unexplored
'''
for x in range(1000): #(-.005, .005, .00001)
    for y in range(1000): #(.00001)
        gps_arr[x][y]=[{"lat": current_lat, "lon": current_lon},1] #[latitude, longitude, -1 = empty space]
        current_lon += .00001
        #pixels[x,y] = colors[str(gps_arr[x][y][1])]
        pixels[x,y] = colors[str(random.randint(1,10))] 
    current_lat -= .00001
    current_lon = -117.882759 #reset at start of longitude
'''


'''
## Select small section of Array for search grid
def SearchArray(x_range, y_range):
    for x in range(500,502): 
        for y in range(950,999): 
            #print gps_arr[x][y][0]['lat'] ,',', gps_arr[x][y][0]['lon']
            pass
'''
'''
33.88184, -117.88278, #11111
33.88184, -117.88277, #11444
33.88184, -117.88276, #11888
33.88184, -117.88275, #11FFF
33.88184, -117.88278, #44111
33.88184, -117.88277, #44444
33.88184, -117.88276, #44888
33.88184, -117.88275, #44FFF
33.88182, -117.88278, #88111
33.88182, -117.88277, #88444
33.88182, -117.88276, #88888
33.88182, -117.88275, #88FFF
33.88181, -117.88278, #DD111
33.88181, -117.88277, #DD444
33.88181, -117.88276, #DD888
33.88181, -117.88275, #DDFFF
33.881825, -117.882759, #FF222
33.881835, -117.882769, #F1111

global measurement_array
        
    ###################################################################################
    ## Measurement Array setup
    half_deg_delta = .00828 # hypo length change every 1/2 degree with 0deg = 1.8m to 45deg = 2.54558  
    measurement_start = 2.54
    for x in range(181):
        if x < 91:
            measurement_array.append(round((measurement_start - (half_deg_delta * x)),5))
        else:
            measurement_array.append(round((measurement_array[x - 1] + half_deg_delta),5))

    #print(measurement_array)


#######################################################################################
    #### GPS Precision within the scanning range of 90degrees from start_scan
    #  Region Map
    #     North
    #   3    |    0
    #        |
    #        |
    # W------------- E
    #        |
    #        |
    #   2    |    1      
    #        S
    #add destination point
    def gps_to_map(self):
        temp_gps_list = []
        if (self.curr_dir > 315):  # check for cross over between region 3 and 0
            self.start_scan = (self.curr_dir + 45) - 360
        else:
            self.start_scan = self.curr_dir + 45

        print(self.start_scan, '***************')

        if (self.start_scan < 90): # if in region 0 ending in region 3
            self.insert_x()
            self.append_x()
            self.insert_y()
        elif (self.start_scan < 180):
            self.insert_y()
            self.append_x()
            self.append_y()
        elif (self.start_scan < 270):
            self.append_x()
            self.append_y()
            self.insert_x()
        else:
            self.append_y()
            self.insert_x()
            self.insert_y()
        # Build dictionary of surrounding Coords with float precision 5

        self.gps_precision = [                             
                            #16 outer points
                            {'lat': 0.00002, 'lon':-0.00002}, {'lat': 0.00001, 'lon':-0.00001}, {'lat': 0, 'lon':0},  {'lat': -0.00001, 'lon':0.00001}]
        
        for x in range(2, -2, -1):
            for y in range(-2, 2, 1):
                temp_gps_list.append(((math.floor((self.current_pos_gps['lat'] + (x*0.00001)) * 10 ** 5)/ 10 ** 5), 
                                    math.floor((self.current_pos_gps['lon'] + (y*0.00001)) * 10 ** 5)/ 10 ** 5))




'''