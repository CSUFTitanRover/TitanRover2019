
import numpy as np
import time, math

_dimx = _dimy = 3
global measurement_array
    
_precision = 0.00001
_boarder = 0.00009 # padded edge for map
fill_val = np.int8(-1)
slam_map = []
scan = []
current_pos_gps = {'lat':0 ,'long': 0}  #(Latitude, Longitude)
org_offset_gps  = {'lat':33.88273 ,'long': -117.88399}
dest_gps        = {'lat':0 ,'long': 0}
#augments the gps after 5 decimal cut
curr_dir = 0


###################################################################################
######## numpy made readible
def fillMap():
    global slam_map, _dimy, _dimx
    slam_map = np.full((_dimy, _dimx), fill_val, dtype=np.int8)
    '''
    dimx = dimy = 3
    example output for np.full((dimy, dimx), -1, dtype=np.int8)
        [[-1. -1. -1.]
        [-1. -1. -1.]
        [-1. -1. -1.]] FYI the dimx and dimy are switched in function call 
    '''

def append_y():
    global slam_map, _dimy, _dimx
    slam_map = np.insert(slam_map, _dimy, fill_val, axis=0)
    _dimy += 1
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

def append_x():
    global slam_map, _dimy, _dimx
    slam_map = np.insert(slam_map, _dimx, fill_val, axis=1)
    _dimx += 1
    '''
    example output for: print(slamit.slam_map); slamit.fill_val = 2; slamit.append_x(); print(slamit.slam_map)
        [[-1 -1 -1] before
        [-1 -1 -1]
        [-1 -1 -1]]
        [[-1 -1 -1  2]  after
        [-1 -1 -1  2]
        [-1 -1 -1  2]]
    '''

def insert_x():
    global slam_map, _dimy, _dimx
    org_offset_gps['long'] = (math.floor((org_offset_gps['long'] - _precision) * 10 ** 5)) / 10 ** 5
    slam_map = np.insert(slam_map, 0, fill_val, axis=1)
    _dimx += 1
    '''
    example output for: print(slamit.slam_map); slamit.fill_val = 2; slamit.insert_x(); print(slamit.slam_map)
        [[-1 -1 -1] before
        [-1 -1 -1]
        [-1 -1 -1]]
        [[ 2 -1 -1 -1]  after
        [ 2 -1 -1 -1]
        [ 2 -1 -1 -1]]
    '''

def insert_y():
    global slam_map, _dimy, _dimx
    org_offset_gps['lat'] = (math.floor((org_offset_gps['lat'] + _precision) * 10 ** 5)) / 10 ** 5
    temp_arr = np.full((1, _dimx), fill_val, dtype=np.int8)
    slam_map = np.insert(temp_arr, 1, slam_map, axis=0)
    _dimy += 1
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
def expand_map():
    global org_offset_gps, _dimy, _dimx, _precision, _boarder
    '''
    import sqlite3
    logindbfile = 'sql_file_name.db'
    conn = sqlite3.connect(logindbfile)
    cur = conn.cursor()
    num_coords = sql size
    '''
    num_coords = 1
    f = open("scoutfile.txt", "r")
    newpoints = 0
        
    for x in range(num_coords):
        newpoints = f.readline()
        newpoints = newpoints.split(', ')
        sql_lat, sql_lon = float(newpoints[0]), float(newpoints[1])
        newgps = gps_trunc(sql_lat, sql_lon)
        print('org_gps ' + str(org_offset_gps) + ' with width and height of ' + str(_dimx))
        if (newgps[0] - _boarder) < (org_offset_gps['lat'] - (_dimy * _precision)):
            print('in first y appending ' + str(int(math.floor((newgps[0] - (org_offset_gps['lat'] -  (_dimy * _precision + _boarder))) * 10 ** 5))))
            for i in range(int(math.floor((newgps[0] - (org_offset_gps['lat'] -  (_dimy * _precision + _boarder))) * 10 ** 5))):
                append_y() #append difference amount
                
        if (newgps[0] + _boarder) > org_offset_gps['lat']:
            print('in second y inserting ' + str(int(math.floor((newgps[0] + _boarder - org_offset_gps['lat'])* 10 ** 5))) + '\n')
            for i in range(int(math.floor((newgps[0] + _boarder - org_offset_gps['lat'])* 10 ** 5))):
                insert_y() #insert difference amount

        # widen the x-plane
        if (newgps[1] + _boarder) > (org_offset_gps['long'] + (_dimx * _precision)):
            print('in first x appending ' + str(int(math.floor(((newgps[1] + _boarder) - (org_offset_gps['long'] + (_dimx * _precision))) * 10 ** 5))))
            for i in range(int(math.floor(((newgps[1] + _boarder) - (org_offset_gps['long'] + (_dimx * _precision))) * 10 ** 5))):
                append_x() #append difference amount
        
        if (newgps[1] - _boarder) < org_offset_gps['long']:
            print('in second x inserting ' + str(int(math.floor((org_offset_gps['long'] - (newgps[1] - _boarder)) * 10 ** 5))) + '\n')
            for i in range(int(math.floor((org_offset_gps['long'] - (newgps[1] - _boarder)) * 10 ** 5))):
                insert_x() #insert difference amount
        
        if x == 0: #3400:
            print('final info')
            print('gps offset start is ' + str(org_offset_gps))
            print('with a height of ' + str(_dimy) + ' and a width of ' + str(_dimx))
            print('final lat is ' + str(org_offset_gps['lat'] - (_dimy * _precision)))
            print('final long is ' + str(org_offset_gps['long'] + (_dimx * _precision)))
            break #exit()

    f.close()

######################################################################################
####### math Truncating to 5 decimal positions without rounding
def gps_trunc(f_lat, f_lon):
    import math
    return math.floor(f_lat * 10 ** 5)/(10 ** 5) , math.floor(f_lon * 10 ** 5)/(10 ** 5)


fillMap()
print(slam_map)
expand_map()
print('\nnew map')
print(slam_map)
