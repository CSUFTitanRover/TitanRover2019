; Auto-generated. Do not edit!


(cl:in-package mobility_topic-msg)


;//! \htmlinclude MultiJoy.msg.html

(cl:defclass <MultiJoy> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (njoys
    :reader njoys
    :initarg :njoys
    :type std_msgs-msg:UInt8
    :initform (cl:make-instance 'std_msgs-msg:UInt8))
   (joys
    :reader joys
    :initarg :joys
    :type (cl:vector sensor_msgs-msg:Joy)
   :initform (cl:make-array 0 :element-type 'sensor_msgs-msg:Joy :initial-element (cl:make-instance 'sensor_msgs-msg:Joy))))
)

(cl:defclass MultiJoy (<MultiJoy>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MultiJoy>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MultiJoy)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mobility_topic-msg:<MultiJoy> is deprecated: use mobility_topic-msg:MultiJoy instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <MultiJoy>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobility_topic-msg:header-val is deprecated.  Use mobility_topic-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'njoys-val :lambda-list '(m))
(cl:defmethod njoys-val ((m <MultiJoy>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobility_topic-msg:njoys-val is deprecated.  Use mobility_topic-msg:njoys instead.")
  (njoys m))

(cl:ensure-generic-function 'joys-val :lambda-list '(m))
(cl:defmethod joys-val ((m <MultiJoy>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobility_topic-msg:joys-val is deprecated.  Use mobility_topic-msg:joys instead.")
  (joys m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MultiJoy>) ostream)
  "Serializes a message object of type '<MultiJoy>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'njoys) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'joys))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'joys))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MultiJoy>) istream)
  "Deserializes a message object of type '<MultiJoy>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'njoys) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'joys) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'joys)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'sensor_msgs-msg:Joy))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MultiJoy>)))
  "Returns string type for a message object of type '<MultiJoy>"
  "mobility_topic/MultiJoy")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MultiJoy)))
  "Returns string type for a message object of type 'MultiJoy"
  "mobility_topic/MultiJoy")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MultiJoy>)))
  "Returns md5sum for a message object of type '<MultiJoy>"
  "d1fe0e1be06cf2ea74daadf46387e623")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MultiJoy)))
  "Returns md5sum for a message object of type 'MultiJoy"
  "d1fe0e1be06cf2ea74daadf46387e623")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MultiJoy>)))
  "Returns full string definition for message of type '<MultiJoy>"
  (cl:format cl:nil "Header header~%std_msgs/UInt8 njoys~%sensor_msgs/Joy[] joys~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/UInt8~%uint8 data~%~%================================================================================~%MSG: sensor_msgs/Joy~%# Reports the state of a joysticks axes and buttons.~%Header header           # timestamp in the header is the time the data is received from the joystick~%float32[] axes          # the axes measurements from a joystick~%int32[] buttons         # the buttons measurements from a joystick ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MultiJoy)))
  "Returns full string definition for message of type 'MultiJoy"
  (cl:format cl:nil "Header header~%std_msgs/UInt8 njoys~%sensor_msgs/Joy[] joys~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/UInt8~%uint8 data~%~%================================================================================~%MSG: sensor_msgs/Joy~%# Reports the state of a joysticks axes and buttons.~%Header header           # timestamp in the header is the time the data is received from the joystick~%float32[] axes          # the axes measurements from a joystick~%int32[] buttons         # the buttons measurements from a joystick ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MultiJoy>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'njoys))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'joys) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MultiJoy>))
  "Converts a ROS message object to a list"
  (cl:list 'MultiJoy
    (cl:cons ':header (header msg))
    (cl:cons ':njoys (njoys msg))
    (cl:cons ':joys (joys msg))
))
