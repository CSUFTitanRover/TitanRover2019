;; Auto-generated. Do not edit!


(when (boundp 'test_topic::Arm)
  (if (not (find-package "TEST_TOPIC"))
    (make-package "TEST_TOPIC"))
  (shadow 'Arm (find-package "TEST_TOPIC")))
(unless (find-package "TEST_TOPIC::ARM")
  (make-package "TEST_TOPIC::ARM"))

(in-package "ROS")
;;//! \htmlinclude Arm.msg.html


(defclass test_topic::Arm
  :super ros::object
  :slots (_J1 _J2 _J3 _J4 _J51 _J52 ))

(defmethod test_topic::Arm
  (:init
   (&key
    ((:J1 __J1) 0)
    ((:J2 __J2) 0)
    ((:J3 __J3) 0)
    ((:J4 __J4) 0)
    ((:J51 __J51) 0)
    ((:J52 __J52) 0)
    )
   (send-super :init)
   (setq _J1 (round __J1))
   (setq _J2 (round __J2))
   (setq _J3 (round __J3))
   (setq _J4 (round __J4))
   (setq _J51 (round __J51))
   (setq _J52 (round __J52))
   self)
  (:J1
   (&optional __J1)
   (if __J1 (setq _J1 __J1)) _J1)
  (:J2
   (&optional __J2)
   (if __J2 (setq _J2 __J2)) _J2)
  (:J3
   (&optional __J3)
   (if __J3 (setq _J3 __J3)) _J3)
  (:J4
   (&optional __J4)
   (if __J4 (setq _J4 __J4)) _J4)
  (:J51
   (&optional __J51)
   (if __J51 (setq _J51 __J51)) _J51)
  (:J52
   (&optional __J52)
   (if __J52 (setq _J52 __J52)) _J52)
  (:serialization-length
   ()
   (+
    ;; int8 _J1
    1
    ;; int8 _J2
    1
    ;; int8 _J3
    1
    ;; int8 _J4
    1
    ;; int8 _J51
    1
    ;; int8 _J52
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _J1
       (write-byte _J1 s)
     ;; int8 _J2
       (write-byte _J2 s)
     ;; int8 _J3
       (write-byte _J3 s)
     ;; int8 _J4
       (write-byte _J4 s)
     ;; int8 _J51
       (write-byte _J51 s)
     ;; int8 _J52
       (write-byte _J52 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _J1
     (setq _J1 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _J1 127) (setq _J1 (- _J1 256)))
   ;; int8 _J2
     (setq _J2 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _J2 127) (setq _J2 (- _J2 256)))
   ;; int8 _J3
     (setq _J3 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _J3 127) (setq _J3 (- _J3 256)))
   ;; int8 _J4
     (setq _J4 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _J4 127) (setq _J4 (- _J4 256)))
   ;; int8 _J51
     (setq _J51 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _J51 127) (setq _J51 (- _J51 256)))
   ;; int8 _J52
     (setq _J52 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _J52 127) (setq _J52 (- _J52 256)))
   ;;
   self)
  )

(setf (get test_topic::Arm :md5sum-) "9b2ff0d79665aaff197a9e50422410bb")
(setf (get test_topic::Arm :datatype-) "test_topic/Arm")
(setf (get test_topic::Arm :definition-)
      "int8 J1
int8 J2
int8 J3
int8 J4
int8 J51
int8 J52

")



(provide :test_topic/Arm "9b2ff0d79665aaff197a9e50422410bb")


