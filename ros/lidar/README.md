# Lidar README
===============================

**_To Run Hector slam along with sick lidar you need to follow the below steps._**


1. Install the following packages for ros kinetic. If you have a different version of ros just replace kinetic with your _"distro"_. 
   **Ex.** ```ros-melodic-hector-slam, ros-lunar-hector-slam.```

```shell

    sudo apt-get install ros-kinetic-hector-slam
    sudo apt-get install ros-kinetic-hector-slam-launch
    sudo apt-get install ros-kinetic-hector-mapping
    sudo apt-get install ros-kinetic-lms1xx

```


2. Follow the Steps from the lidar directory (eg. ~/home/$user/catkin_ws/src/lidar):

```shell

    sudo mv /opt/ros/kinetic/share/hector_slam_launch/rviz_cfg/mapping_demo.rviz /opt/ros/kinetic/share/hector_slam_launch/rviz_cfg/mapping_demo.rviz.bak
    sudo cp mapping_demo.rviz /opt/ros/kinetic/share/hector_slam_launch/rviz_cfg/

```


3. Now you need to change the tutorial.launch file in hector_slam_launch:

```Shell

    roscd hector_slam_launch/launch
    sudo nano tutorial.launch

```


4. Add the following lines of code at the end but before ```</launch>``` tag:
 
```Shell

    <node pkg="tf" type="static_transform_publisher" name="map_baselink_broadcaster" args="0 0 0 0 0 0 map base_link 100"/>
    <node pkg="tf" type="static_transform_publisher" name="baselink_laser_broadcaster" args="0 0 0 0 0 0 base_link laser 100"/>

```

also at the top change this line ```<param name="/use_sim_time" value="true"/>``` so that it says ```<param name="/use_sim_time" value="false"/>```


5. Now we need to change the mapping_default.launch file in hector_mapping:

```Shell

    roscd hector_mapping/launch
    sudo nano mapping_default.launch

```


6. Change the mapping_default.launch to use the following configuration instead of the default configuration.

```Shell

    <param name="map_frame" value="map" />
    <param name="base_frame" value="base_link" />
    <param name="odom_frame" value="base_link" />

```


7. Finally go to the lidar directory in your catkin workspace and run the command. Make sure you have ```roscore``` already running in a seperate terminal:

```Shell

    roslaunch sick_lidar.launch

```

You can now see the lidar output along with hector slam which generates a Map.