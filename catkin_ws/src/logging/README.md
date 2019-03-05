# ROS Logging

This implementation will use Python object to extent ROS logging services. 

ROS current logging levels:
>   DEBUG
>   INFO
>   WARN
>   ERROR
>   FATAL

Using this logger a custom filter of log data will be available.

```python
object(log level, node, message) = rospy.info("message")
ex. imuLog('info', 'imu', 'IMU starting Calibration')
```
GUI filter display OUTPUT:
```
 INFO Log - [IMU]
 IMU starting Calibratoin
 Empty
 Empty
 
 WARN Log - [IMU]
 Empty

 DEGUB Log - [IMU]
 Empty

 Error Log - [IMU]
 Empty
 Empty
 Empty

 FATAL Log - [IMU]
 Empty
 ```
 


