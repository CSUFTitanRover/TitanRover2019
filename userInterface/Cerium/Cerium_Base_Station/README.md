# Titan Rover - Cerium Base Station


## Questions

David Feinzimer `dfeinzimer@csu.fullerton.edu`



## Requirements

Python 2.x

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

1) `cd ~/catkin_ws/src/fake_sensor_test/launch`

2) `roslaunch fake.launch`


### 3) Start the onboard communication interface (development or production mode):

1. `cd ~/TitanRover2019/userInterface/Cerium/Cerium_Base_Station/`

2. `python listener.py`

3. If the port is already taken, find the PID and kill it with steps 5 and 6

4. `sudo lsof -i:9600`

5. `sudo kill <PID>`


### 4) Start the base station interface:

1) `cd ~/TitanRover2019/userInterface/Cerium/Cerium_Base_Station`

2) `export ROS_MASTER_URI="http://192.168.1.2:11311/"` # Vehicle's IP

3) `export ROS_IP="192.168.1.204"` # Connecting machine

4) `export ROS_HOSTNAME="192.168.1.204"` # Connecting machine

5) `python main.py`



## Important Technical Notes

1) Socket connections are currently killed if a connection fails after 1 second.



## Engineering / Design Notes

1) For Google Maps screenshots we're using the largest 100 zoom level with
browser zoom set to 100%

2) --- URGENT ISSUES ---

2.1) Everything locks if no ROS Master is running

3) --- NEXT DEVELOPMENTS ---

3.1) Publish to mode topic/Stop publish to mode topic

3.2) Expanded rostopic viewer

3.3) Decide on final database file path.

3.4) Routinely search for new ball records and add them as landmarks.

4) --- NEEDS FIXING / IMPROVEMENTS ---

4.1) Program will not start if ROS is not running

4.2) Rover icon is blitting even if GNSS topis is not connected.



## Problems & Solutions

1) Message import errors?

1.1) `sudo nano ~/.bashrc`

1.2) Add the following to bottom of the file:

1.3) `source ~/catkin_ws/devel/setup.bash`
