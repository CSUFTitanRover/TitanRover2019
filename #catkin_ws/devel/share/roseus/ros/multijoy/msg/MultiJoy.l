;; Auto-generated. Do not edit!


(when (boundp 'multijoy::MultiJoy)
  (if (not (find-package "MULTIJOY"))
    (make-package "MULTIJOY"))
  (shadow 'MultiJoy (find-package "MULTIJOY")))
(unless (find-package "MULTIJOY::MULTIJOY")
  (make-package "MULTIJOY::MULTIJOY"))

(in-package "ROS")
;;//! \htmlinclude MultiJoy.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass multijoy::MultiJoy
  :super ros::object
  :slots (_header _njoys _joys ))

(defmethod multijoy::MultiJoy
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:njoys __njoys) (instance std_msgs::UInt8 :init))
    ((:joys __joys) (let (r) (dotimes (i 0) (push (instance sensor_msgs::Joy :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _njoys __njoys)
   (setq _joys __joys)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:njoys
   (&rest __njoys)
   (if (keywordp (car __njoys))
       (send* _njoys __njoys)
     (progn
       (if __njoys (setq _njoys (car __njoys)))
       _njoys)))
  (:joys
   (&rest __joys)
   (if (keywordp (car __joys))
       (send* _joys __joys)
     (progn
       (if __joys (setq _joys (car __joys)))
       _joys)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; std_msgs/UInt8 _njoys
    (send _njoys :serialization-length)
    ;; sensor_msgs/Joy[] _joys
    (apply #'+ (send-all _joys :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; std_msgs/UInt8 _njoys
       (send _njoys :serialize s)
     ;; sensor_msgs/Joy[] _joys
     (write-long (length _joys) s)
     (dolist (elem _joys)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; std_msgs/UInt8 _njoys
     (send _njoys :deserialize buf ptr-) (incf ptr- (send _njoys :serialization-length))
   ;; sensor_msgs/Joy[] _joys
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _joys (let (r) (dotimes (i n) (push (instance sensor_msgs::Joy :init) r)) r))
     (dolist (elem- _joys)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get multijoy::MultiJoy :md5sum-) "d1fe0e1be06cf2ea74daadf46387e623")
(setf (get multijoy::MultiJoy :datatype-) "multijoy/MultiJoy")
(setf (get multijoy::MultiJoy :definition-)
      "Header header
std_msgs/UInt8 njoys
sensor_msgs/Joy[] joys
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: std_msgs/UInt8
uint8 data

================================================================================
MSG: sensor_msgs/Joy
# Reports the state of a joysticks axes and buttons.
Header header           # timestamp in the header is the time the data is received from the joystick
float32[] axes          # the axes measurements from a joystick
int32[] buttons         # the buttons measurements from a joystick 

")



(provide :multijoy/MultiJoy "d1fe0e1be06cf2ea74daadf46387e623")


