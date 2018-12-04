; Auto-generated. Do not edit!


(cl:in-package test_mobility-msg)


;//! \htmlinclude joystick.msg.html

(cl:defclass <joystick> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (mobility
    :reader mobility
    :initarg :mobility
    :type test_mobility-msg:Mobility
    :initform (cl:make-instance 'test_mobility-msg:Mobility))
   (arm
    :reader arm
    :initarg :arm
    :type test_mobility-msg:Arm
    :initform (cl:make-instance 'test_mobility-msg:Arm))
   (mode
    :reader mode
    :initarg :mode
    :type test_mobility-msg:Mode
    :initform (cl:make-instance 'test_mobility-msg:Mode)))
)

(cl:defclass joystick (<joystick>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <joystick>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'joystick)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test_mobility-msg:<joystick> is deprecated: use test_mobility-msg:joystick instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_mobility-msg:header-val is deprecated.  Use test_mobility-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'mobility-val :lambda-list '(m))
(cl:defmethod mobility-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_mobility-msg:mobility-val is deprecated.  Use test_mobility-msg:mobility instead.")
  (mobility m))

(cl:ensure-generic-function 'arm-val :lambda-list '(m))
(cl:defmethod arm-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_mobility-msg:arm-val is deprecated.  Use test_mobility-msg:arm instead.")
  (arm m))

(cl:ensure-generic-function 'mode-val :lambda-list '(m))
(cl:defmethod mode-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_mobility-msg:mode-val is deprecated.  Use test_mobility-msg:mode instead.")
  (mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <joystick>) ostream)
  "Serializes a message object of type '<joystick>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'mobility) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'arm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'mode) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <joystick>) istream)
  "Deserializes a message object of type '<joystick>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'mobility) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'arm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'mode) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<joystick>)))
  "Returns string type for a message object of type '<joystick>"
  "test_mobility/joystick")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'joystick)))
  "Returns string type for a message object of type 'joystick"
  "test_mobility/joystick")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<joystick>)))
  "Returns md5sum for a message object of type '<joystick>"
  "ed6711036913a5609081e2c7ac5cd927")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'joystick)))
  "Returns md5sum for a message object of type 'joystick"
  "ed6711036913a5609081e2c7ac5cd927")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<joystick>)))
  "Returns full string definition for message of type '<joystick>"
  (cl:format cl:nil "Header header~%Mobility mobility~%Arm arm~%Mode mode~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: test_mobility/Mobility~%int8 ForwardY~%int8 TurningX~%~%================================================================================~%MSG: test_mobility/Arm~%int8 J1~%int8 J2~%int8 J3~%int8 J4~%int8 J51~%int8 J52~%~%================================================================================~%MSG: test_mobility/Mode~%int8 mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'joystick)))
  "Returns full string definition for message of type 'joystick"
  (cl:format cl:nil "Header header~%Mobility mobility~%Arm arm~%Mode mode~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: test_mobility/Mobility~%int8 ForwardY~%int8 TurningX~%~%================================================================================~%MSG: test_mobility/Arm~%int8 J1~%int8 J2~%int8 J3~%int8 J4~%int8 J51~%int8 J52~%~%================================================================================~%MSG: test_mobility/Mode~%int8 mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <joystick>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'mobility))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'arm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'mode))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <joystick>))
  "Converts a ROS message object to a list"
  (cl:list 'joystick
    (cl:cons ':header (header msg))
    (cl:cons ':mobility (mobility msg))
    (cl:cons ':arm (arm msg))
    (cl:cons ':mode (mode msg))
))
