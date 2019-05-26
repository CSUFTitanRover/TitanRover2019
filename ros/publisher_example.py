from gnss.msg import gps

msg = gps() #message variable
rospy.init_node('gnss') #create and name current node
gps_pub = rospy.Publisher('/gnss', gps, queue_size=1) #create the publisher object that will publish message of type gps to the node named '/gnss'
rate = rospy.Rate(20) #not necessary but changes the rate that you publish data

#do your magic to get the tennis ball gps
msg.roverLat = ''
msg.roverLon = ''
msg.tennisLat = "" #latitude as a string
msg.tennisLon = "" #longitude as a string

gps_pub.publish(msg) #publish msg to the node

