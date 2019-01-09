#!/bin/bash

roslaunch rosbridge_server rosbridge_websocket.launch &
cd ~/TitanRover2019/Cerium; python -m SimpleHTTPServer &
cd ~/TitanRover2019/Cerium; python appbaseESC.py
