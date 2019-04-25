#!/usr/bin/env python3.5
import sys, subprocess, sqlite3
import threading #, keyboard
import sys, time, signal, socket, rospy
from math import floor
import math
from gnss.msg import gps
#from sensor_msgs.msg import LaserScan
from finalimu.msg import fimu
#from fake_sensor_test.msg import gps
#from fake_sensor_test.msg import imu

rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from driver import Driver as myDriver
#from roverdb import Database

__gps = (0.00, 0.00)
__nextWaypoint = (0.00, 0.00)
__distance = 0.0

######################################################################################
# System Requirement of one argument for process instructions
if len (sys.argv) != 2 :
    print("Usage: Run Command Missing ")
    sys.exit (1)

mode_info = None
acceleration = 0
curr_pos = (0,0,'0',0)

# def connect():
#     #msg = gps()
#     #gps_pub = rospy.Publisher('/gnss', gps, queue_size=1)
#     #rospy.init_node('gnss')
#     #rate = rospy.Rate(100) # 10hz
#     #msg.header.frame_id = 'GNSS'

#     global curr_pos
#     host = "Rover_TR.local" #"192.168.1.117" 
#     port = 9091
#     BUFFER_SIZE = 1024

#     Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#     Client.connect((host, port))

#     while True:
#         try:
#             #MESSAGE = raw_input("Enter : ")
#             #Client.send(MESSAGE)     
#             data = Client.recv(BUFFER_SIZE)
#             data = data.split(b' ')
#             #print(" Client received data:", float(data[4]), ' ', float(data[5]))
#             curr_pos = (float(data[4]), float(data[5]))
#             msg.lat, msg.lon = curr_pos[0], curr_pos[1]
#             gps_pub.publish(msg)
#         except:
#             Client.close()
#             break

#####################################################################################
## File I/O from https://www.g-loaded.eu/2016/11/24/how-to-terminate-running-python-threads-using-signals/
#####################################################################################
class Job(threading.Thread):
    _file = None

    def __init__(self, sf):
        self._file = sf
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
        rospy.init_node('listener', anonymous=True)

    def callback(self, data):
        global db, curr_pos, acceleration

        curr_position = str(gps_trunc(float(data.roverLat))) + ', ' + str(gps_trunc(float(data.roverLon))) + ', primary, ' + str(acceleration) + '\n'
        curr_pos = gps_trunc(float(data.roverLat)), gps_trunc(float(data.roverLon)), 'primary', acceleration
        '''
        if keyboard.is_pressed('q'):
            curr_pos = gps_trunc(data.roverLat) + ', ' + gps_trunc(data.roverLon) + ', primary, ' + acceleration
        else:
            curr_pos = gps_trunc(data.roverLat) + ', ' + gps_trunc(data.roverLon) + ', breadcrumb' + acceleration
        '''

        self._file.write(curr_position)
        #db.insertMap(map, curr_pos[0], curr_pos[1], curr_pos[2], curr_pos[3])

    def update_acceleration(self, data):
        global acceleration
        #acceleration = data.accel
        acceleration = data.yaw.pitch
         
    def run(self):
        global curr_pos
        print('Thread #%s started' % self.ident)
 
        while not self.shutdown_flag.is_set():            
            #rospy.Subscriber("gnss", gps, self.callback)
            #rospy.Subscriber("imu", fimu, update_acceleration)
            rospy.Subscriber("gnss", gps, self.callback)
            rospy.Subscriber("imu", fimu, self.update_acceleration)
            time.sleep(0.5)
 
        print('Thread #%s stopped' % self.ident)

class ServiceExit(Exception):
    pass

def service_shutdown(signum, frame):
    global scoutfile
    scoutfile.write("closing\n")
    scoutfile.close()
    print('Caught signal %d' % signum)
    raise ServiceExit

def start_scouting(sf):
    print("Scouting has begun")
    #rospy.init_node('listener', anonymous=True)
    #rospy.Subscriber("mode", mobility, mode_update)
    #rospy.Subscriber("imu", fimu, update_acceleration)
    #rospy.Subscriber("gnss", gps_position, store_info)
    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)
    print('Starting main program')
 
    try:
        j1 = Job(sf)
        j1.start()
               
        while True:
            time.sleep(0.5)

    except ServiceExit:
        j1.shutdown_flag.set()
        j1.join()
                
    print('Exiting main program')

def gps_trunc(coord):
    return floor(coord * 10 ** 5)/(10 ** 5)



def mode_update(data):
    global mode_info
    mode_info = data.data

def parse_map_file():
    global __gps, __nextWaypoint
    pathfile = open("pathfile.txt", "w")
    print('Parsing the Scout file')
    #erase dup and 5 dec
    #use distance between points and remove 3m
    f = open("scoutfile.txt","r")
    try:
        while True: #not EOFError:
            location = f.readline()
            location = location.split(", ")
            __gps = float(location[0]), float(location[1])
            __gps = __nextWaypoint =  (floor(__gps[0] * 10 ** 5)/(10 ** 5) , floor(__gps[1] * 10 ** 5)/(10 ** 5))
            pathfile.write(str(__gps[0]) + ', ' + str(__gps[1]) + '\n')
            setDistance()
            while __distance < 300: #and not EOFError:  #distance in cm
                location = f.readline()
                location = location.split(", ")
                __nextWaypoint = float(location[0]), float(location[1])
                __nextWaypoint =  (floor(__nextWaypoint[0] * 10 ** 5)/(10 ** 5) , floor(__nextWaypoint[1] * 10 ** 5)/(10 ** 5))
                setDistance()

            #write __gps to db
        #write __nextWaypoint to db
    except:
        print('Closing pathfile.txt')
        pathfile.close()

def setDistance():
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


#add button to catch tennis ball point
def ballMotherFucker():
    while True:
        pass
        


if __name__ == '__main__':
    #db = Database()
    if sys.argv[1] == 'scout':
        # gps_data = threading.Thread(target= connect)
        # gps_data.start()
        
        scoutfile = open("scoutfile.txt", "w")
        start_scouting(scoutfile)

    elif sys.argv[1] == 'parse':
        parse_map_file()
    else:
        print('Unknown argument: "' + sys.argv[1] + '"' )
        exit()


'''
33.882440 , -117.883611
33.881991 , -117.883712
33.881974 , -117.883878
33.881874 , -117.884192
33.881984 , -117.884443
33.881987 , -117.884439
33.882019 , -117.884517
33.882209 , -117.884571
33.882223 , -117.884577
33.882638 , -117.884322
33.882641 , -117.883943
33.882554 , -117.883688
33.882440 , -117.883611
'''

