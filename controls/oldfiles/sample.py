import rospy
from gnss.msg import gps
from finalimu.msg import fimu
global heading, gps
heading = 0.0
gps = (0.0, 0.0)

def headingdata(data):
	global heading
	heading = 12.222 #float(data.Yaw.yaw)
	print(heading)

def gpsdata(data):
	global gps
	gps = (1.2, 2.4) #(float(data.roverLat), float(data.roverLon))
	print(gps)


rospy.init_node('listener', anonymous=True)

while True:
	#rospy.init_node('listener', anonymous=True)
	global gps, heading
#	rospy.Subscriber("gnss", gps, gpsdata)
	rospy.Subscriber("imu", fimu, headingdata)
	print("heading", heading)
	print("gps", gps)
	#rospy.spin()

#main()
