#!/usr/bin/env python
import rospy
import message_filters as mf
from multijoy.msg import MultiJoy
from sensor_msgs.msg import Joy

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
        msg=MultiJoy()
        msg.header.stamp=rospy.Time.now()
        msg.njoys.data=self.njoys
        msg.joys=args
        self.multijoy_pub.publish(msg)

        if self.debug:
            rospy.loginfo('joys retrieved and published')

if __name__=='__main__':
    rospy.init_node('multijoy_node')
    parser=MultiJoyParser()
    rospy.spin()
