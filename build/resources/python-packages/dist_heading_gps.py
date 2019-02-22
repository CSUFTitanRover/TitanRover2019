import math, sys

R = 6378.1 #Radius of the Earth
brng = 0
dist = 0

def main(lat, lon, bearing, bearing_type, distance, measurement_type):
    R = 6378.1 #Radius of the Earth
    lat1, lon1 = float(lat), float(lon)
    lat2, lon2 = 0.0 , 0.0
    brng = 1.52 # float(bearing)
    dist = float(distance)

    print(brng)
    print(type(brng))

    if(bearing_type not in ('rad' , 'deg')):
        print('Usage Error: bearing type must be deg(for degrees) or rad(for radians) ')
        exit()
    elif(measurement_type not in ('mm','cm','m','km')):
        print('Usage Error: measurement type must be mm, cm, m, km')
        exit()

    # Bearing must be in radians
    if(bearing_type == 'rad' and brng >= 0.0 and brng < 6.28319):
        brng = bearing
    elif(bearing_type == 'deg' and brng >= 0.0 and brng < 360.0):
        brng = math.radians(brng)
        lat1 = math.radians(lat1) #Current lat point converted to radians
        lon1 = math.radians(lon1) #Current long point converted to radians
    else:
        print('Bearing out of range')
        exit()
    
    # Distance must be in km    
    if measurement_type == 'mm':
        dist = dist / 1000000
    elif measurement_type == 'cm':
        dist = dist / 100000
    elif measurement_type == 'm':
        dist = dist / 1000
    elif measurement_type == 'km':
        dist = dist

    print(math.cos(brng))

    lat2 = math.asin( math.sin(lat1)*math.cos(dist/R) + math.cos(lat1)*math.sin(dist/R)*math.cos(brng))
    
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(dist/R)*math.cos(lat1), math.cos(dist/R)-math.sin(lat1)*math.sin(lat2))

    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)

    return ((lat2, lon2))

if __name__ == '__main__':
    if len(sys.argv) != 7:
        print('Invalid or missing arguments: pass current_pos, bearing, bearing_type, dist, measurement_dist')
        exit()
       
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])


#brng = 1.57 #Bearing is 90 degrees converted to radians.
#d = 15 #Distance in km

#lat2  52.20444 - the lat result I'm hoping for
#lon2  0.36056 - the long result I'm hoping for.







