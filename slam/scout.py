#!/usr/bin/env python

import threading
import sys, time, signal, socket
######################################################################################
# System Requirement of one argument for process instructions
if len (sys.argv) != 2 :
    print("Usage: Run Command Missing ")
    sys.exit (1)

#import rospy
#from sensor_msgs.msg import LaserScan
#from finalimu.msg import fimu

mode_info = None
acceleration = 0
curr_pos = {0,0}

def connect():
    global curr_pos
    host = "192.168.1.116" 
    port = 9091
    BUFFER_SIZE = 4096 

    Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    Client.connect((host, port))

    while True:
        try:
            #MESSAGE = raw_input("Enter : ")
            #Client.send(MESSAGE)     
            data = Client.recv(BUFFER_SIZE)
            data = data.split(b' ')
            print(data)
            #data = pickle.loads(data)
            #print(" Client received data:", float(data[4]), ' ', float(data[5]))
            curr_pos = float(data[4]), float(data[5])

        except:
            Client.close()
            break

#####################################################################################
## File I/O from https://www.g-loaded.eu/2016/11/24/how-to-terminate-running-python-threads-using-signals/
#####################################################################################
class Job(threading.Thread):
    _file = None

    def __init__(self, sf):
        self._file = sf
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
  
    def run(self):
        global curr_pos
        print('Thread #%s started' % self.ident)
 
        while not self.shutdown_flag.is_set():
            #self._file.write("hello" + " " + "world" + "\n")
            self._file.write(str(curr_pos) + "\n")
            #scoutfile.write(data.pos)
            #print(data.pos + ' ' + acceleration + '\n')
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

def update_acceleration(data):
    global acceleration
    acceleration = data.accel

def mode_update(data):
    global mode_info
    mode_info = data.data

def parse_map_file():
    print('Parsing the Scout file')



if __name__ == '__main__':
    if sys.argv[1] == 'scout':
        gps_data = threading.Thread(target = connect)
        gps_data.start()
        
        scoutfile = open("scoutfile.txt", "w")
        start_scouting(scoutfile)
    elif sys.argv[1] == 'parse':
        parse_map_file()
    else:
        print('Unknown argument: "' + sys.argv[1] + '"' )
        exit()

