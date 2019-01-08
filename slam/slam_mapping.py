#Timothy Parks mock slam design
# 2d array 3281 x 3281 ft
# 2d array 1000 x 1000 m
# precision to 0.00001 about 1m

import random, time, math
import numpy as np
from geopy.distance import geodesic
from geopy.distance import distance

## Global Variables
# dim's must be odd number size and form square for initialization 
dimx = dimy = 3
fill_val = np.int8(-1)
precision = 0.00001
slam_map = []
measurement_array = []
scan = []
current_pos_gps = (0 , 0)  #(Latitude, Longitude)
org_offset_gps  = (0 , 0)
dest_gps        = (0 , 0)

###################################################################################
######## numpy made readible
def fillMap():
    global dimx, dimy, fill_val
    return np.full((dimy, dimx), fill_val, dtype=np.int8)

# example output for np.full((4, 3), -1, dtype=np.int8)
'''[[-1. -1. -1.]
    [-1. -1. -1.]  <----- Not the same output for this function
    [-1. -1. -1.]  <----- the array matches the np call example only
    [-1. -1. -1.]]
FYI the dimx and dimy are switched in function call '''

def append_y():
    global dimy, slam_map, fill_val
    dimy += 1
    return np.insert(slam_map, dimy - 1, fill_val, axis=0)

# example output for np.insert(arr, arr[0].size , 2, axis=0)
'''[[-1. -1. -1.]
    [-1. -1. -1.]
    [-1. -1. -1.]
    [ 2.  2.  2.]]'''

def append_x():
    global dimx, slam_map, fill_val
    dimx += 1
    return np.insert(slam_map, dimx - 1, fill_val, axis=1)

# example output for np.insert(arr, arr[0].size , 2, axis=1)
'''[[-1. -1. -1.  2.]
    [-1. -1. -1.  2.]
    [-1. -1. -1.  2.]]'''

def insert_x():
    global dimy, slam_map, fill_val
    return np.insert(slam_map, 0, fill_val, axis=1)
    
def insert_y():
    global dimx, slam_map, fill_val
    temp_arr = np.full((1, dimx), fill_val, dtype=np.int8)
    return np.insert(temp_arr, 1, slam_map, axis=0)

#Other 2D array design
# gps_arr = [[0 for x in range(1000)] for y in range(1000)] 
######################################################################################
####### LiDAR Update
def scan_update()
    global scan
    

######################################################################################
##  Contour Map setup
def make_map_image():
    from PIL import Image
    img = Image.new('RGB', (1000,1000), 'black')
    pixels = img.load()

    ##  Contour Map coloring ranges
    colors = {'-1':(211,211,211), '1':(255,255,255),'2':(255,204,204),'3':(255,153,153),
                '4':(255,102,102),'5':(255,51,51),'6':(255,0,0),'7':(204,0,0),'8':(153,0,0),
                '9':(102,0,0),'10':(51,0,0), '11':(0,0,0)}

    #img.show()
    #img.save('rover_map','png')
    #print('image written')
#######################################################################################

def start_init():
    global slam_map, current_long, current_lat, scan, dimx, dimy, measurement_array
    ###################################################################################
    ## GPS Array Creation
    # Array of default size populated with fill_val  
    slam_map = fillMap()

    ## test points to prepare array
    current_long = -117.882759 # horizontal Fullerton E21 Backdoor
    current_lat = 33.881825  #vertical Fullerton E21 Backdoor
    #lat_update = .005 
    #array_offset_x , array_offset_y = current_lat - precision, current_long

    ## Grid Offset start location latitude
    if current_lat > 0:
        current_lat += ((dimx - 1)/2) * precision
    else:
        current_lat -= ((dimx - 1)/2) * precision

    ## Grid Offset start location longitude
    current_long -= ((dimy - 1)/2) * precision

    ###################################################################################
    ## Measurement Array setup
    half_deg_delta = .00828 # hypo length change every 1/2 degree with 0deg = 1.8m to 45deg = 2.54558  
    measurement_start = 2.54
    measurement_array = []
    for x in range(181):
        if x < 91:
            measurement_array.append(round((measurement_start - (half_deg_delta * x)),5))
        else:
            measurement_array.append(round((measurement_array[x - 1] + half_deg_delta),5))

    #print(measurement_array)

def update_sensors():
    #get IMU
    #get current GPS
    #get lidar scan
    

def main():
    global slam_map, current_long, current_lat, scan, dimx, dimy, measurement_array
    update_sensors()
    






    

    #print(distance(current_pos_gps, dest_gps).cm)

if __name__ == '__main__':
    start_init()
    #need ros spin
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
        gps_arr[x][y]=[{"lat": current_lat, "lon": current_long},1] #[latitude, longitude, -1 = empty space]
        current_long += .00001
        #pixels[x,y] = colors[str(gps_arr[x][y][1])]
        pixels[x,y] = colors[str(random.randint(1,10))] 
    current_lat -= .00001
    current_long = -117.882759 #reset at start of longitude
'''


'''
## Select small section of Array for search grid
def SearchArray(x_range, y_range):
    for x in range(500,502): 
        for y in range(950,999): 
            #print gps_arr[x][y][0]['lat'] ,',', gps_arr[x][y][0]['lon']
            pass
'''

