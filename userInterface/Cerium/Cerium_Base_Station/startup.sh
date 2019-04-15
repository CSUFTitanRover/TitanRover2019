#!/bin/bash

# TODO This script does not work and needs to be fixed/tested

export ROS_MASTER_URI="http://192.168.1.2:11311/"   # Vehicle
echo $ROS_MASTER_URI

export ROS_IP="192.168.1.203"                       # Connecting machine
echo $ROS_IP  

export ROS_HOSTNAME="192.168.1.203"		               # Connecting machine
echo $ROS_HOSTNAME
