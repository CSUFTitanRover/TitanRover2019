# Titan Rover - Cerium Base Station



## Questions
  David Feinzimer `dfeinzimer@csu.fullerton.edu`



## Requirements
  Python3
  
  Pygame 1.9.4
  
  ROS Kinetic or ROS Melodic


  
## Usage
   Start onboard IMU: 
       1) `cd ~/catkin_ws/src/finalimu/src/`
       2) `python cal_run_Imu.py`

   Start onbord interface:
       1) `cd ~/TitanRover2019/userInterface/Cerium_Base_Station/`
       2) `python listener.py`
       2a) If the port is already taken, find the PID and kill it: 
           `sudo lsof -i:9600` 
            and 
           `sudo kill <PID>`

   Start base interface:
       1) `cd ~/TitanRover2019/userInterface/Cerium_Base_Station`
       2) `export ROS_MASTER_URI="http://192.168.1.2:11311/"` # Vehicle's IP
       3) `export ROS_IP="192.168.1.203"` # Connecting machine
       4) `export ROS_HOSTNAME="192.168.1.203"` # Connecting machine
       5) `python3 main.py`
