
import numpy as np
import time

_dimx = _dimy = 3
global measurement_array
    
_precision = 0.00001
_boarder = 0.00009 # padded edge for map
fill_val = np.int8(-1)
slam_map = []
scan = []
current_pos_gps = {'lat':0 ,'long': 0}  #(Latitude, Longitude)
org_offset_gps  = {'lat':33.88273223 ,'long': -117.883993178}
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

def insert_x(new_offset_long):
    global slam_map, _dimy, _dimx
    org_offset_gps['long']  = new_offset_long
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

def insert_y(new_offset_lat):
    global slam_map, _dimy, _dimx
    org_offset_gps['lat']  = new_offset_lat
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
    num_coords = 8381
    f = open("scoutfile.txt", "r")
    newpoints = 0


    for x in range(num_coords):
        newpoints = f.readline()
        newpoints = newpoints.split(', ')
        sql_lat, sql_lon = float(newpoints[0]), float(newpoints[1])
        newgps = gps_trunc(sql_lat, sql_lon)
        
        # widen the y_plane
        if newgps[0] > org_offset_gps['lat'] - (_dimx * _precision + _boarder):
            for i in range(int(abs(newgps[0] - (org_offset_gps['lat'] - (_dimx * _precision + _boarder)))) * 10 ** 5):
                append_y() #append difference amount
        elif newgps[0] < org_offset_gps['lat'] + _boarder:
            for i in range(int(((org_offset_gps['lat'] + _boarder) - newgps[0]) * 10 ** 5)):
                insert_y(newgps[0]) #insert difference amount
        
        '''
            org_offset_gps  = {'lat':33.88273223 ,'long': -117.883993178}
            newgps = 33.882762293, -117.88399565
            _dimx = _dimy = 3
            _precision = 0.00001
            _boarder = 0.00009 # padded edge for map
        '''

        # widen the x-plane
        if newgps[1] > org_offset_gps['long'] + (_dimy * _precision - _boarder):
            print(int(abs(abs(org_offset_gps['long'] + (_dimy * _precision + _boarder)) - abs(newgps[1])) * 10 ** 5))
            print(org_offset_gps['long'])
            print(org_offset_gps['long'] + (_dimy * _precision + _boarder))
            print(newgps[1])
            print(str(_dimx) + ' ' + str(_dimy))
            print('')
            for i in range(int(abs(abs(org_offset_gps['long'] + (_dimy * _precision + _boarder)) - abs(newgps[1])) * 10 ** 5)):
                
                append_x() #append difference amount
        elif newgps[1] < org_offset_gps['long'] - _boarder:
            print('elif long')
            print(org_offset_gps['long'])
            print(str(_dimx) + ' ' + str(_dimy))
            print('')
            for i in range(int(abs(abs(newgps[1]) - abs(org_offset_gps['long'] - _boarder)) * 10 ** 5 )):
                insert_x(newgps[1]) #insert difference amount
        
        if x == 100: #3400:
            exit()

    f.close()

######################################################################################
####### math Truncating to 5 decimal positions without rounding
def gps_trunc(f_lat, f_lon):
    import math
    return math.floor(f_lat * 10 ** 5)/(10 ** 5) , math.floor(f_lon * 10 ** 5)/(10 ** 5)


fillMap()
print(slam_map)
expand_map()
print(str(_dimx) + ' ' + str(_dimy))
