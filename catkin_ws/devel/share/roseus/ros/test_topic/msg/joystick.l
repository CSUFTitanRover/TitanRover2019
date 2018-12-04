;; Auto-generated. Do not edit!


(when (boundp 'test_topic::joystick)
  (if (not (find-package "TEST_TOPIC"))
    (make-package "TEST_TOPIC"))
  (shadow 'joystick (find-package "TEST_TOPIC")))
(unless (find-package "TEST_TOPIC::JOYSTICK")
  (make-package "TEST_TOPIC::JOYSTICK"))

(in-package "ROS")
;;//! \htmlinclude joystick.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass test_topic::joystick
  :super ros::object
  :slots (_header _mobility _arm _mode ))

(defmethod test_topic::joystick
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:mobility __mobility) (instance test_topic::Mobility :init))
    ((:arm __arm) (instance test_topic::Arm :init))
    ((:mode __mode) (instance test_topic::Mode :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _mobility __mobility)
   (setq _arm __arm)
   (setq _mode __mode)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:mobility
   (&rest __mobility)
   (if (keywordp (car __mobility))
       (send* _mobility __mobility)
     (progn
       (if __mobility (setq _mobility (car __mobility)))
       _mobility)))
  (:arm
   (&rest __arm)
   (if (keywordp (car __arm))
       (send* _arm __arm)
     (progn
       (if __arm (setq _arm (car __arm)))
       _arm)))
  (:mode
   (&rest __mode)
   (if (keywordp (car __mode))
       (send* _mode __mode)
     (progn
       (if __mode (setq _mode (car __mode)))
       _mode)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; test_topic/Mobility _mobility
    (send _mobility :serialization-length)
    ;; test_topic/Arm _arm
    (send _arm :serialization-length)
    ;; test_topic/Mode _mode
    (send _mode :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; test_topic/Mobility _mobility
       (send _mobility :serialize s)
     ;; test_topic/Arm _arm
       (send _arm :serialize s)
     ;; test_topic/Mode _mode
       (send _mode :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; test_topic/Mobility _mobility
     (send _mobility :deserialize buf ptr-) (incf ptr- (send _mobility :serialization-length))
   ;; test_topic/Arm _arm
     (send _arm :deserialize buf ptr-) (incf ptr- (send _arm :serialization-length))
   ;; test_topic/Mode _mode
     (send _mode :deserialize buf ptr-) (incf ptr- (send _mode :serialization-length))
   ;;
   self)
  )

(setf (get test_topic::joystick :md5sum-) "ed6711036913a5609081e2c7ac5cd927")
(setf (get test_topic::joystick :datatype-) "test_topic/joystick")
(setf (get test_topic::joystick :definition-)
      "Header header
Mobility mobility
Arm arm
Mode mode

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
MSG: test_topic/Mobility
int8 ForwardY
int8 TurningX

================================================================================
MSG: test_topic/Arm
int8 J1
int8 J2
int8 J3
int8 J4
int8 J51
int8 J52

================================================================================
MSG: test_topic/Mode
int8 mode

")



(provide :test_topic/joystick "ed6711036913a5609081e2c7ac5cd927")


