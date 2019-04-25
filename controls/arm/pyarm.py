import serial
import time
import rospy
from multijoy.msg import MultiJoy
from sensor_msgs.msg import Joy


mapAxes = { 'J1' : {-1 : ('s05e', 's07e'), 1 : ('s04e', 's07e'), 0 : ('s06e', 's06e')},
            'J2' : {-1 : ('s15e', 's17e'), 1 : ('s14e', 's17e'), 0 : ('s16e', 's16e')}
            }

global stat1, stat4, stat51, stat52
stat1 = False
stat4 = False
stat51 = False
stat52 = False

def armData(data):
    global stat1, stat4, stat51, stat52
    j1 = int(data.joys[0].axes[4])
    j4 = int(data.joys[0].axes[5])
    j51 = (data.joys[0].buttons[5], data.joys[0].buttons[7])        # (left, right)
    j52 = (data.joys[0].buttons[4], data.joys[0].buttons[6])        # (close, open)

    for i in range(2):
        if not stat1 and j1 is not 0:
            ser.write(mapAxes['J1'][j1][i])
            stat1 = True
        else:
            ser.write(mapAxes['J1'][j1][i])
            stat1 = False

        if not stat4 and j4 is not 0:
            ser.write(mapAxes['J2'][j4][i])
            stat4 = True
        else:
            ser.write(mapAxes['J2'][j4][i])
            stat4 = False
    
    if j51[0] is 1 and j51[1] is 0 and not stat51:
        ser.write("s24e")
        ser.write("s27e")
        stat51 = True
    elif j51[0] is 0 and j51[1] is 1 and not stat51:
        ser.write("s25e")
        ser.write("s27e")
        stat51 = True
    elif j51[0] is 0 and j51[1] is 0:
        ser.write("s26e")
        stat51 = False

    if j52[0] is 1 and j52[1] is 0 and not stat52:
        ser.write("s34e")
        ser.write("s37e")
        stat52 = True
    elif j52[0] is 0 and j52[1] is 1 and not stat52:
        ser.write("s35e")
        ser.write("s37e")
        stat52 = True
    elif j52[0] is 0 and j52[1] is 0:
        ser.write("s36e")
        stat52 = False
    

def main():
    rospy.Subscriber('/multijoy', MultiJoy, armData)
    rospy.spin()

if __name__ == "__main__":
    ser = serial.Serial("/dev/serial/by-id/usb-Silicon_Labs_reach_9000-if00-port0", baudrate=115200)
    rospy.init_node("listener")
    main()
