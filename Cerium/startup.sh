#!/bin/bash

source /opt/ros/kinetic/setup.bash; roslaunch rosbridge_server rosbridge_websocket.launch &
cd /home/ubuntu/TitanRover2019/Cerium/; /usr/bin/python -m SimpleHTTPServer &
/home/ubuntu/TitanRover2019/Cerium/appbaseESC.py
