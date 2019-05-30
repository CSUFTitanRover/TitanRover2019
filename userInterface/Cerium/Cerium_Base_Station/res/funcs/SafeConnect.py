import rospy

# This function returns a roscore connection. It will only attempt a connection
# once it has detected that roscore is running.

def SafeConnect():
    try:
        print "Cerium is connecting to ROS, please wait."
        rospy.get_master().getPid()
        # If an exception was not thrown, establish a connection.
        status = rospy.init_node('listener', anonymous=True)
        return status
    except:
        print "Cerium cannot start due to a roscore issue."
        print "Please check the roscore configuration."
        exit()

# def SafeConnect():
#     state = False
#     while state == False:
#         try:
#             # Check if roscore is running
#             rospy.get_master().getPid()
#             # If an exception was not raised, then roscore is running.
#             state = True
#         except:
#             print "roscore is not connected. Please start roscore."
#             state = False
#         if state == True:
#             # If an exception was not raised, connect and return.
#             status = rospy.init_node('listener', anonymous=True)
#             return status
