#Timothy Parks mock slam design
# 2d array 3281 x 3281 ft
# 2d array 1000 x 1000 m
# precision to 0.00001 about 1m

import random, time, math
import numpy as np

global slam_map
# dim's must be odd number size and form square for initialization 
global dimx # Starting x size of array map
global dimy # Starting y size of array map
dimx = dimy = 3
global fill_val # Fill val of unexplored space
fill_val = np.int8(-1)
global precision 
precision = 0.00001

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



###################################################################################
##  Contour Map setup
from PIL import Image
img = Image.new('RGB', (1000,1000), 'black')
pixels = img.load()

##  Contour Map coloring ranges
colors = {'-1':(211,211,211), '1':(255,255,255),'2':(255,204,204),'3':(255,153,153),
            '4':(255,102,102),'5':(255,51,51),'6':(255,0,0),'7':(204,0,0),'8':(153,0,0),
            '9':(102,0,0),'10':(51,0,0), '11':(0,0,0)}
###################################################################################
## GPS Array Creation
# Array of default size populated with fill_val  
slam_map = fillMap()

## test points to prepare array
start_lon = -117.882759 # horizontal Fullerton E21 Backdoor
start_lat = 33.881825  #vertical Fullerton E21 Backdoor
#lat_update = .005 
#array_offset_x , array_offset_y = start_lat - precision, start_lon

## Grid Offset start location latitude
if start_lat < 0:
    start_lat += ((dimx - 1)/2) * precision
else:
    start_lat -= ((dimx - 1)/2) * precision

## Grid Offset start location longitude
if start_lat > 0:
    start_lon += ((dimy - 1)/2) * precision
else:
    start_lon -= ((dimy - 1)/2) * precision




## prepopulated with GPS points based on start as unexplored
'''
for x in range(1000): #(-.005, .005, .00001)
    for y in range(1000): #(.00001)
        gps_arr[x][y]=[{"lat": start_lat, "lon": start_lon},1] #[latitude, longitude, -1 = empty space]
        start_lon += .00001
        #pixels[x,y] = colors[str(gps_arr[x][y][1])]
        pixels[x,y] = colors[str(random.randint(1,10))] 
    start_lat -= .00001
    start_lon = -117.882759 #reset at start of longitude
'''




###################################################################################
## Measurement Array setup
half_deg_delta = .00828 # hypo length change every 1/2 degree with 0deg = 1.8m to 45deg = 2.54558  
scan_start = 2.54
scan = []
for x in range(181):
    if x < 91:
        scan.append(round((scan_start - (half_deg_delta * x)),5))
    else:
        scan.append(round((scan[x - 1] + half_deg_delta),5))

print(scan)



'''
## Select small section of Array for search grid
def SearchArray(x_range, y_range):
    for x in range(500,502): 
        for y in range(950,999): 
            #print gps_arr[x][y][0]['lat'] ,',', gps_arr[x][y][0]['lon']
            pass
'''

#img.show()
# img.save('rover_map','png')
# print('image written')