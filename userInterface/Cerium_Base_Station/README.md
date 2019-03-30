# Titan Rover - Cerium Base Station



## Questions
  David Feinzimer `dfeinzimer@csu.fullerton.edu`



## Requirements
  Python3
  
  Pygame 1.9.4
  
  ROS Kinetic or ROS Melodic


  
## Usage
   Make sure onboard software is up to date:
       1) `cd ~/TitanRover2019/`
       2) `git pull`

   Start onboard IMU: 
       1) `cd ~/catkin_ws/src/finalimu/src/`
       2) `python cal_run_Imu.py`

   Start onboard GPS: 
       1) ?

   Start onboard interface:
       1) `cd ~/TitanRover2019/userInterface/Cerium_Base_Station/`
       2) `python listener.py`
       2a) If the port is already taken, find the PID and kill it: 
           `sudo lsof -i:9600` 
            and 
           `sudo kill <PID>`
   
   Prepare base interface:
       1) In main.py set value: `display_LAT_TL`
       2) In main.py set value: `display_LON_TL`
       3) In main.py set value: `display_LAT_BR`
       4) In main.py set value: `display_LON_BR`
       5) In main.py set value: `mode` to `prod`
 
   Start base interface:
       1) `cd ~/TitanRover2019/userInterface/Cerium_Base_Station`
       2) `export ROS_MASTER_URI="http://192.168.1.2:11311/"` # Vehicle's IP
       3) `export ROS_IP="192.168.1.203"` # Connecting machine
       4) `export ROS_HOSTNAME="192.168.1.203"` # Connecting machine
       5) `python3 main.py`
