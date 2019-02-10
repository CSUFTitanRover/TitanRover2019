# Cerium - Web

Updated: 2.9.19.2
Author: David Feinzimer dfeinzimer@csu.fullerton.edu
Description: A web based, mobile friendly solution for driving Titan Rover.

Setup:
	1) Ensure correct 'ros->url' value in cerium.html.
	2) Ensure correct 'camera' value in the <body> tag. of cerium.html.
	3) Ensure roscore and a proper ESC (appbaseESC.py for the Runt) file is running
	4) To launch Cerium manually open 3 terminals and run one of the following
	   commands in each.
			1) roslaunch rosbridge_server rosbridge_websocket.launch
			2) sudo python -m SimpleHTTPServer
			3) python appbaseESC.py

Problems & Solutions:
	Motion not displaying camera feed:
		1) Add 'modprobe bcm2835-v4l2' to /etc/rc.local
		2) Or simply run 'sudo modprobe bcm2835-v4l2'
	Sourcing:
		source ~/ros_catkin_ws/devel/setup.bash
	MASTER URI Set:
		export ROS_MASTER_URI=http://...
	Updating files:
		sudo scp -r ~/localpath/Cerium/Web pi@IP:~/Cerium/
	Modifying/adding startup scripts:
		nano ~/.bashrc
	Killing an existing SimpleHTTPServer port:
		1) Find the PID using the port: sudo lsof -i:8000
		2) Kill it: kill XXXX

Dependencies & Related Documentation:
	rosbridge_server
		wiki.ros.org/rosbridge_server
	roslbjs
		github.com/RobotWebTools/roslibjs
	Motion
		motion-project.github.io
