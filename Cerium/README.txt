# Cerium - Web

Web solution for rover control.

README Version:
	1.29.19.1

Author(s):
	David Feinzimer dfeinzimer@csu.fullerton.edu

Setup:
	1) Ensure correct 'ros->url' value
	2) Ensure correct 'camera' value
	3) Ensure roscore and a proper ESC file is running
	4) Tab Layout:
			1) roslaunch rosbridge_server rosbridge_websocket.launch
			2) sudo python -m SimpleHTTPServer
			3) python appbaseESC.py
			4) [OPTIONAL] rostopic echo /joy/0


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
