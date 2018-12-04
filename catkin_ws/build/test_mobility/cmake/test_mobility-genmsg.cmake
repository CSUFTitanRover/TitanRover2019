# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "test_mobility: 4 messages, 0 services")

set(MSG_I_FLAGS "-Itest_mobility:/home/nvidia/catkin_ws/src/test_mobility/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(test_mobility_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg" NAME_WE)
add_custom_target(_test_mobility_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "test_mobility" "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg" ""
)

get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg" NAME_WE)
add_custom_target(_test_mobility_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "test_mobility" "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg" ""
)

get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg" NAME_WE)
add_custom_target(_test_mobility_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "test_mobility" "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg" ""
)

get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg" NAME_WE)
add_custom_target(_test_mobility_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "test_mobility" "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg" "test_mobility/Arm:test_mobility/Mobility:test_mobility/Mode:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test_mobility
)
_generate_msg_cpp(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test_mobility
)
_generate_msg_cpp(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test_mobility
)
_generate_msg_cpp(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg"
  "${MSG_I_FLAGS}"
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test_mobility
)

### Generating Services

### Generating Module File
_generate_module_cpp(test_mobility
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test_mobility
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(test_mobility_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(test_mobility_generate_messages test_mobility_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_cpp _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_cpp _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_cpp _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_cpp _test_mobility_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_mobility_gencpp)
add_dependencies(test_mobility_gencpp test_mobility_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_mobility_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test_mobility
)
_generate_msg_eus(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test_mobility
)
_generate_msg_eus(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test_mobility
)
_generate_msg_eus(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg"
  "${MSG_I_FLAGS}"
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test_mobility
)

### Generating Services

### Generating Module File
_generate_module_eus(test_mobility
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test_mobility
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(test_mobility_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(test_mobility_generate_messages test_mobility_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_eus _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_eus _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_eus _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_eus _test_mobility_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_mobility_geneus)
add_dependencies(test_mobility_geneus test_mobility_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_mobility_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test_mobility
)
_generate_msg_lisp(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test_mobility
)
_generate_msg_lisp(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test_mobility
)
_generate_msg_lisp(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg"
  "${MSG_I_FLAGS}"
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test_mobility
)

### Generating Services

### Generating Module File
_generate_module_lisp(test_mobility
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test_mobility
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(test_mobility_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(test_mobility_generate_messages test_mobility_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_lisp _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_lisp _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_lisp _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_lisp _test_mobility_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_mobility_genlisp)
add_dependencies(test_mobility_genlisp test_mobility_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_mobility_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test_mobility
)
_generate_msg_nodejs(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test_mobility
)
_generate_msg_nodejs(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test_mobility
)
_generate_msg_nodejs(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg"
  "${MSG_I_FLAGS}"
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test_mobility
)

### Generating Services

### Generating Module File
_generate_module_nodejs(test_mobility
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test_mobility
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(test_mobility_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(test_mobility_generate_messages test_mobility_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_nodejs _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_nodejs _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_nodejs _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_nodejs _test_mobility_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_mobility_gennodejs)
add_dependencies(test_mobility_gennodejs test_mobility_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_mobility_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test_mobility
)
_generate_msg_py(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test_mobility
)
_generate_msg_py(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test_mobility
)
_generate_msg_py(test_mobility
  "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg"
  "${MSG_I_FLAGS}"
  "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg;/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test_mobility
)

### Generating Services

### Generating Module File
_generate_module_py(test_mobility
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test_mobility
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(test_mobility_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(test_mobility_generate_messages test_mobility_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Arm.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_py _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mode.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_py _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/Mobility.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_py _test_mobility_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/catkin_ws/src/test_mobility/msg/joystick.msg" NAME_WE)
add_dependencies(test_mobility_generate_messages_py _test_mobility_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_mobility_genpy)
add_dependencies(test_mobility_genpy test_mobility_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_mobility_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test_mobility)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test_mobility
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(test_mobility_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test_mobility)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test_mobility
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(test_mobility_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test_mobility)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test_mobility
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(test_mobility_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test_mobility)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test_mobility
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(test_mobility_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test_mobility)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test_mobility\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test_mobility
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(test_mobility_generate_messages_py std_msgs_generate_messages_py)
endif()
