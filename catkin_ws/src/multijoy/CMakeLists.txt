cmake_minimum_required(VERSION 2.8.3)
project(multijoy)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  std_msgs
  message_generation
  )

add_message_files(
  FILES
  MultiJoy.msg
  )

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
  )

catkin_package(
  CATKIN_DEPENDS message_runtime
  )

include_directories(
  ${catkin_INCLUDE_DIRS}
  )
