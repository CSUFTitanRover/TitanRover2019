# Titan Rover - Cerium Base Station


## Questions

David Feinzimer `dfeinzimer@csu.fullerton.edu`



## Requirements

Python3

Pygame 1.9.4

ROS Kinetic or ROS Melodic



## Usage

### 1) Make sure the onboard and base station software is up to date:

1) On both machines, perform the following commands:

2) `cd ~/TitanRover2019/`

3) `git pull`


### 2) [OPTION A] If the desired mode is production, start the onboard IMU and GNSS

1) `cd ~/catkin_ws/src/finalimu/src/`

2) `python cal_run_Imu.py`

3) `cd ~/catkin_ws/src/gnss/src/`

4) `python reach.py`


### 2) [OPTION B] If the desired mode is development, start the simulated IMU and GNSS publisher:

1) `~/catkin_ws/src/fake_sensor_test/launch`

2) `roslaunch fake.launch`


### 3) Start the onboard communication interface (development or production mode):

1. `source ~/catkin_ws/devel/setup.bash`

2. `cd ~/TitanRover2019/userInterface/Cerium/Cerium_Base_Station/`

3. `python listener.py`

4. If the port is already taken, find the PID and kill it with steps 5 and 6

5. `sudo lsof -i:9600`

6. `sudo kill <PID>`


### 4) Prepare the base station interface:

1) In main.py set value: `display_LAT_TL`

2) In main.py set value: `display_LON_TL`

3) In main.py set value: `display_LAT_BR`

4) In main.py set value: `display_LON_BR`

5) In main.py set value: `mode` to `prod`

6) In main.py set value: `map_image` to `SETTING_CSUF` or `SETTING_VICT`


### 5) Start the base station interface:

1) `cd ~/TitanRover2019/userInterface/Cerium/Cerium_Base_Station`

2) `source ~/catkin_ws/devel/setup.bash`

3) `export ROS_MASTER_URI="http://192.168.1.2:11311/"` # Vehicle's IP

4) `export ROS_IP="192.168.1.204"` # Connecting machine

5) `export ROS_HOSTNAME="192.168.1.204"` # Connecting machine

6) `python main.py`
