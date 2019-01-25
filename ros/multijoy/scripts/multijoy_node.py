#!/usr/bin/env python
import rospy, socket, struct, serial, threading, paramiko
import message_filters as mf
from multijoy.msg import MultiJoy
from sensor_msgs.msg import Joy

base_ubiquiti = "192.168.1.201"
hostName = socket.gethostname()
print("Host: " + hostName)

def getRSSI():
    global RSSI
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(base_ubiquiti, username="admin", password="titanrover17")
    while not rospy.is_shutdown():
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("mca-status | grep signal")
        signal = ssh_stdout.readlines()[0]
        signal = int('-' + ''.join(i for i in signal if i.isdigit()))
        RSSI = signal

def putRF(data):                            #arguments to make function more self-contained and function-like
    rf_uart = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_Base433_0001-if00-port0', 19200, timeout=.01)
    rf_uart.setDTR(True)                    #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
    rf_uart.setRTS(True)                    #then these two lines will send low logic to both which puts the module in transmit mode 0

    if not rf_uart.cts:                     #Check if both send and receive buffers are empty
        rf_uart.write(b's' + data + b'f')   #start byte + payload + stop byte
        rf_uart.flush() 
        return len(data)                 #waits until all data is written
    else:
        return -1

def putSock(oData):
    try:
        port = 8888  # Make sure it's within the > 1024 $$ <65535 range
        rover = "192.168.1.2"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("s")
        s.connect((rover, port))
        print("connected")
        s.send(oData)
        print('Sent: ' + oData)
        s.close()
    except:
        print("Error in putSock()")

def packDEEZNUTZ(message, joyNum): #object to bytes
    try:
        return struct.pack(\
        'iibbbbbbbbbbbbbbbbbb',\
        message.header.stamp.secs,\
        message.header.stamp.nsecs,\
        int(message.joys[joyNum].axes[0] * 127),\
        int(message.joys[joyNum].axes[1] * 127),\
        int(message.joys[joyNum].axes[2] * 127),\
        int(message.joys[joyNum].axes[3] * 127),\
        int(message.joys[joyNum].axes[4] * 127),\
        int(message.joys[joyNum].axes[5] * 127),\
        message.joys[joyNum].buttons[0],\
        message.joys[joyNum].buttons[1],\
        message.joys[joyNum].buttons[2],\
        message.joys[joyNum].buttons[3],\
        message.joys[joyNum].buttons[4],\
        message.joys[joyNum].buttons[5],\
        message.joys[joyNum].buttons[6],\
        message.joys[joyNum].buttons[7],\
        message.joys[joyNum].buttons[8],\
        message.joys[joyNum].buttons[9],\
        message.joys[joyNum].buttons[10],\
        message.joys[joyNum].buttons[11])
    except:
        print("Error in D")

class MultiJoyParser(object):
    
    def __init__(self):

        # Retrieve parameters
        self.ns=rospy.get_name()
	self.param_name_debug=self.ns+'/debug'
        self.param_name_njoys=self.ns+'/njoys'
        if rospy.has_param(self.param_name_debug):
            self.debug=rospy.get_param(self.param_name_debug)
        else:
            self.debug=False
        self.njoys=rospy.get_param(self.param_name_njoys)

        if self.debug:
            rospy.loginfo('debug={}'.format(self.debug))
            rospy.loginfo('njoys={}'.format(self.njoys))
            
        # Setup ros publisher
        self.multijoy_pub=rospy.Publisher('/multijoy', MultiJoy, queue_size=1)

        # Setup ros subscribers
        self.joy_subs=[mf.Subscriber('/joy/'+str(i),Joy, queue_size=1) for i in xrange(self.njoys)]
        self.timeSync=mf.ApproximateTimeSynchronizer(self.joy_subs, 10, self.njoys*100)
        self.timeSync.registerCallback(self.update)



    def update(self, *args):
        global RSSI
        msg=MultiJoy()
        msg.header.stamp=rospy.Time.now()
        if (hostName == "tegra-ubuntu"):
            msg.source = 0
        else:
            msg.source = 1
        msg.njoys.data=self.njoys
        msg.joys=args
        print(msg)

        print(RSSI)
        if(RSSI > -70) or hostName == "tegra-ubuntu":
            self.multijoy_pub.publish(msg)
        else:
            putRF(packDEEZNUTZ(msg, 0))
        if self.debug:
            rospy.loginfo('joys retrieved and published')

if __name__=='__main__':
    RSSI = 0
    if(hostName != "tegra-ubuntu"):
        threading.Thread(target=getRSSI).start()

    rospy.init_node('multijoy_node')
    parser=MultiJoyParser()
    rospy.spin()
