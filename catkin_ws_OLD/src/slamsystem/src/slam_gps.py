

gps_arr = [[0 for x in range(1000)] for y in range(1000)]
# 2d array 3281 x 3281 ft
# 2d array 1000 x 1000 m
# precision to 0.00001 about 1m
start_lon = -117.882759 # horizontal Fullerton E21 Backdoor
start_lat = 33.881825  #vertical Fullerton E21 Backdoor
lat_update = .005
start_lat += lat_update
for x in range(1000): #(-.005, .005, .00001)
    for y in range(1000): #(.00001)
        gps_arr[x][y]=[{"lat": start_lat, "lon": start_lon},-1]
        start_lon += .00001
    start_lat -= .00001
    start_lon = -117.882759
for x in range(500,502): #(-.005, .005, .00001)
    for y in range(950,999): #(.00001)
        print gps_arr[x][y][0]['lat'] ,',', gps_arr[x][y][0]['lon']
