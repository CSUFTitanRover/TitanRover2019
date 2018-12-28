#Timothy Parks mock slam design
import random, time
from PIL import Image
img = Image.new('RGB', (1000,1000), 'black')
pixels = img.load()
colors = {'-1':(211,211,211), '1':(255,255,255),'2':(255,204,204),'3':(255,153,153),
            '4':(255,102,102),'5':(255,51,51),'6':(255,0,0),'7':(204,0,0),'8':(153,0,0),
            '9':(102,0,0),'10':(51,0,0), '11':(0,0,0)}
gps_arr = [[0 for x in range(1000)] for y in range(1000)] # Empty array unexplored

# 2d array 3281 x 3281 ft
# 2d array 1000 x 1000 m
# precision to 0.00001 about 1m

start_lon = -117.882759 # horizontal Fullerton E21 Backdoor
start_lat = 33.881825  #vertical Fullerton E21 Backdoor
lat_update = .005
start_lat += lat_update

for j in range(10):
    for x in range(1000): #(-.005, .005, .00001)
        for y in range(1000): #(.00001)
            gps_arr[x][y]=[{"lat": start_lat, "lon": start_lon},1] #[latitude, longitude, -1 = empty space]
            start_lon += .00001
            #pixels[x,y] = colors[str(gps_arr[x][y][1])]
            pixels[x,y] = colors[str(random.randint(1,10))]
        start_lat -= .00001
        start_lon = -117.882759 #reset at start of longitude

    '''
    for x in range(500,502): #(-.005, .005, .00001)
        for y in range(950,999): #(.00001)
            #print gps_arr[x][y][0]['lat'] ,',', gps_arr[x][y][0]['lon']
            pass
    '''
    #img.show()
    img.save('rover_map','png')
    print('image written')
    time.sleep(5)