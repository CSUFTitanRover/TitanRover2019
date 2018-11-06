# BNO055 IMU

**To Run the IMU in ROS:**
```shell
  Sync the ROS GitHub with the catkin environment
  Update catkin workspace with "catkin_make"
  cd to IMU folder under ex. catkin_ws/src/imu
  python3.5 src/cal_run_Imu.py
```
--------------------------------------------------------
### ROS IMU dependancies

**roscore is REQUIRED TO BE RUNNING**

std_mgs - Standard Messages

geo_mgs - Geometry Messages

--------------------------------------------------------

### Viewing the ROS IMU output

The program runs the IMU calibration sequence prior to operation. Once the calibration is complete all IMU values can be retrieved with:

>rostopic echo imu
