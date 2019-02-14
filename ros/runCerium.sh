source /home/nvidia/catkin_ws/devel/setup.bash && rosrun mobility roverESC.py &
source /home/nvidia/catkin_ws/devel/setup.bash && rosrun mobility lights.py &
source /home/nvidia/catkin_ws/devel/setup.bash && roslaunch rosbridge_server rosbridge_websocket.launch &
cd /home/nvidia/TitanRover2019/Cerium && sudo python -m SimpleHTTPServer && nvidia &
