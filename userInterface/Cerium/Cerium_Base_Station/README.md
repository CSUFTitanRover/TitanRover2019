# Titan Rover - Cerium Base Station



## Requirements

Python 2.x

Pygame 1.9.4

ROS Kinetic or ROS Melodic



## Usage

### 1) Make sure the onboard and base station software is up to date:

1) On both machines, perform the following command:

2) `cd ~/TitanRover2019/ && git pull`



### 2) [OPTION A] If the desired mode is production, start the onboard IMU and GNSS

1) `cd ~/catkin_ws/src/finalimu/src/ && python cal_run_Imu.py`

2) `cd ~/catkin_ws/src/gnss/src/ && python reach.py`



### 2) [OPTION B] If the desired mode is development, start the simulated IMU and GNSS publisher:

1) `cd ~/catkin_ws/src/fake_sensor_test/launch && roslaunch fake.launch`



### 3) Start the onboard communication interface (development or production mode):

3.1) `cd ~/TitanRover2019/userInterface/Cerium/Cerium_Base_Station/ && python Communicator.py`

3.2) If the port is already taken, find the PID and kill it with steps 3 and 4

3.3) `sudo lsof -i:9600`

3.4) `sudo kill <PID>`



### 4) Start the base station interface:

4.1) `export ROS_MASTER_URI="http://192.168.1.78:11311/"`

4.1) `export ROS_IP="192.168.1.78"` # Connecting machine

4.2) `export ROS_HOSTNAME="192.168.1.78"` # Connecting machine

4.3) `cd ~/TitanRover2019/userInterface/Cerium/Cerium_Base_Station/ && python Cerium.py`



## Important Technical Notes

1) Socket connections are currently killed if a connection fails after 1 second.



## Engineering / Design Notes

1) For Google Maps screenshots we're using the largest 100 zoom level with
browser zoom set to 100%

2) --- URGENT ISSUES ---

2.1) Connect buttons to publishers.

2.2) Ensure correct HINT conversions for all coord formats.

2.3) Add map tiles for HAB site

2.4) Enhance gnss and imu fake data for better testing

3) --- NEXT DEVELOPMENTS ---

3.1) ------ Menu System ------

3.1.a) --------- Delete last entered hint.

3.1.b) --------- Publish to mode topic.

3.1.c) --------- rostopic view

3.2) Routinely search for new ball records and add them as landmarks.

4) --- NEEDS FIXING / IMPROVEMENTS ---

4.1) ------ Rover icon is blitting even if GNSS topic is not connected.

4.2) ------ Enhance coordinate input validation

4.3) ------ On no ROS connection enhance error message

## Problems & Solutions

1) Message import errors?

1.1) `sudo nano ~/.bashrc`

1.2) Add the following to bottom of the file:

1.3) `source ~/catkin_ws/devel/setup.bash`



## Questions

David Feinzimer `dfeinzimer@csu.fullerton.edu`
