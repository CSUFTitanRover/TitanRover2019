# Titan Rover - Cerium Base Station



## Requirements ----------------------------------------------------------------

Python 2.x

Pygame 1.9.4

ROS Kinetic or ROS Melodic



## Usage -----------------------------------------------------------------------

### 1) If the desired mode is dev, start the simulated IMU and GNSS publisher:

1.a) `cd ~/catkin_ws/src/fake_sensor_test/launch && roslaunch fake.launch`



### 2) Start the base station interface:

2.1) `export ROS_MASTER_URI="http://<MASTER'S_IP>:11311/"`

2.2) `cd ~/TitanRover2019/userInterface/Cerium/Cerium_Base_Station/ && python Cerium.py`



## Engineering / Design Notes --------------------------------------------------

7) --- URGENT ISSUES ---

7.2) Add compass.

7.3) Add map tiles (most detailed first).

8) --- NEXT DEVELOPMENTS ---

8.1) ------ Menu System ------

8.1.a) --------- Show more gnss and imu data.

8.1.b) --------- Delete last entered hint.

3.1.c) --------- Publish to mode topic.

9) --- NEEDS FIXING / IMPROVEMENTS ---

9.1) ------ Rover icon is blitting even if GNSS topic is not connected.

9.2) ------ Enhance coordinate input validation

9.3) ------ On no ROS connection enhance error message

9.4) ------ Routinely search for new ball records in /tball and add them as landmarks.

9.5) ------ Database hint submission over ros or socket working.

9.6) ------ Enhance gnss and imu fake data for better testing



## Problems & Solutions --------------------------------------------------------

10) Message import errors?

10.1) `sudo nano ~/.bashrc`

10.2) Add the following to bottom of the file:

10.3) `source ~/catkin_ws/devel/setup.bash`



## Test Points -----------------------------------------------------------------

ECS Bathroom Courtyard

----DD 33.881966°, -117.882964°

----DDM 33°52.918' N, 117°52.9778' W

----DMS 33°52'55.08" N, 117°52'58.668" W

Duke's Facilities

----DD 38.375490°, -110.708199°

----DDM 38°22.5294' N, 110°42.4919' W

----DMS 38°22'31.764" N, 110°42'29.514" W



## Deploying -------------------------------------------------------------------

Upload rover `cd ~/TitanRover2019/userInterface/Cerium && scp -r ./Cerium_Base_Station/ nvidia@192.168.1.2:/home/nvidia/TitanRover2019/userInterface/Cerium/`

Upload base `cd ~/TitanRover2019/userInterface/Cerium && scp -r ./Cerium_Base_Station/ roverbase@192.168.1.3:/home/roverbase/TitanRover2019/userInterface/Cerium/`



## Questions -------------------------------------------------------------------

David Feinzimer `dfeinzimer@csu.fullerton.edu`
