from std_msgs.msg import String
import rospy

def PublishGeneric(topic, message):
    function_name = "PublishGeneric("+topic+", "+message+")"
    pub = rospy.Publisher(topic, String, queue_size=10)
    pub.publish(message)
