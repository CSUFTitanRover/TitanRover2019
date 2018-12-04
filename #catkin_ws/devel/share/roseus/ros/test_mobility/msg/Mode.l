;; Auto-generated. Do not edit!


(when (boundp 'test_mobility::Mode)
  (if (not (find-package "TEST_MOBILITY"))
    (make-package "TEST_MOBILITY"))
  (shadow 'Mode (find-package "TEST_MOBILITY")))
(unless (find-package "TEST_MOBILITY::MODE")
  (make-package "TEST_MOBILITY::MODE"))

(in-package "ROS")
;;//! \htmlinclude Mode.msg.html


(defclass test_mobility::Mode
  :super ros::object
  :slots (_mode ))

(defmethod test_mobility::Mode
  (:init
   (&key
    ((:mode __mode) 0)
    )
   (send-super :init)
   (setq _mode (round __mode))
   self)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:serialization-length
   ()
   (+
    ;; int8 _mode
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _mode
       (write-byte _mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _mode
     (setq _mode (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _mode 127) (setq _mode (- _mode 256)))
   ;;
   self)
  )

(setf (get test_mobility::Mode :md5sum-) "418c02483a8ca57215fb7b31c5c87234")
(setf (get test_mobility::Mode :datatype-) "test_mobility/Mode")
(setf (get test_mobility::Mode :definition-)
      "int8 mode

")



(provide :test_mobility/Mode "418c02483a8ca57215fb7b31c5c87234")


