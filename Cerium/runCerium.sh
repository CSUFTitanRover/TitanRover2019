# Updated: 2.9.19.23.14
# Author: Georden Grabuskie ggrabuskie@csu.fullerton.edu
# Author: David Feinzimer dfeinzimer@csu.fullerton.edu
# Description: This file is intended to allow for easy Cerium startup on the
#              rover. It is recommened that this file be placed in the home
#              directory on the rover.

source /home/nvidia/catkin_ws/devel/setup.bash && rosrun mobility roverESC.py &
source /home/nvidia/catkin_ws/devel/setup.bash && rosrun mobility lights.py &
source /home/nvidia/catkin_ws/devel/setup.bash && roslaunch rosbridge_server rosbridge_websocket.launch &
cd /home/nvidia/TitanRover2019/Cerium && sudo python -m SimpleHTTPServer &
sudo motion &
