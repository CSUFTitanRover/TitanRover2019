cd ~/catkin_ws && source ./devel/setup.bash
export ROS_MASTER_URI=http://$(ifconfig | grep -o 192.168.1.[1-9][0-9][0-9] | head -1):11311 && export ROS_IP=$(ifconfig | grep -o 192.168.1.[1-9][0-9][0-9] | head -1) && export ROS_HOSTNAME=$(ifconfig | grep -o -m1 192.168.1.[1-9][0-9][0-9] | head -1)
source ~/.bashrc
echo $ROS_MASTER_URI
echo $ROS_IP
echo $ROS_HOSTNAME
