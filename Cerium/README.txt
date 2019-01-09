
# Cerium - Web

Web solution for rover control.

Author(s):
	David Feinzimer dfeinzimer@csu.fullerton.edu

Setup:
	1) Ensure correct 'ros->url' value
	2) Ensure correct 'camera' value
	3) Tab Layout:
			1) roscore
			2) rostopic echo /joy/0
			3) roslaunch rosbridge_server rosbridge_websocket.launch
			5) sudo python -m SimpleHTTPServer

Problems & Solutions:
	Motion:
		1) Add 'modprobe bcm2835-v4l2' to /etc/rc.local
		2) Or simply run 'sudo modprobe bcm2835-v4l2'
	Sourcing:
		source ~/ros_catkin_ws/devel/setup.bash
	MASTER URI Set:
		export ROS_MASTER_URI=http://...
	Updating files:
		sudo scp -r ~/localpath/Cerium/Web pi@IP:~/Cerium/

Dependencies & Related Documentation:
	rosbridge_server
		http://wiki.ros.org/rosbridge_server
	roslbjs
		https://github.com/RobotWebTools/roslibjs
