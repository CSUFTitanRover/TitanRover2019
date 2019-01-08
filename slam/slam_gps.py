#Timothy Parks mock slam design
# 2d array 3281 x 3281 ft
# 2d array 1000 x 1000 m
# precision to 0.00001 about 1m

import random, time, math

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
# Empty array 
gps_arr = [[0 for x in range(1000)] for y in range(1000)] 

## test points to prepare array
start_lon = -117.882759 # horizontal Fullerton E21 Backdoor
start_lat = 33.881825  #vertical Fullerton E21 Backdoor
lat_update = .005 
array_offset_x , array_offset_y = start_lat, start_lon

## Grid Offset start location
if start_lat < 0:
    start_lat += lat_update
else:
    start_lat -= lat_update

## prepopulated with GPS points based on start as unexplored
for x in range(1000): #(-.005, .005, .00001)
    for y in range(1000): #(.00001)
        gps_arr[x][y]=[{"lat": start_lat, "lon": start_lon},1] #[latitude, longitude, -1 = empty space]
        start_lon += .00001
        #pixels[x,y] = colors[str(gps_arr[x][y][1])]
        pixels[x,y] = colors[str(random.randint(1,10))] 
    start_lat -= .00001
    start_lon = -117.882759 #reset at start of longitude

###################################################################################
## Measurement Array setup
half_deg_delta = .008284 # hypo length change every 1/2 degree with 0deg = 1.8m to 45deg = 2.54558  
scan_start = 2.54
scan = []
for x in range(241):
    if x < 121:
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
img.save('rover_map','png')
print('image written')
time.sleep(5)