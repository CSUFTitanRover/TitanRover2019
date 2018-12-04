;; Auto-generated. Do not edit!


(when (boundp 'mobility_topic::Mode)
  (if (not (find-package "MOBILITY_TOPIC"))
    (make-package "MOBILITY_TOPIC"))
  (shadow 'Mode (find-package "MOBILITY_TOPIC")))
(unless (find-package "MOBILITY_TOPIC::MODE")
  (make-package "MOBILITY_TOPIC::MODE"))

(in-package "ROS")
;;//! \htmlinclude Mode.msg.html


(defclass mobility_topic::Mode
  :super ros::object
  :slots (_mode ))

(defmethod mobility_topic::Mode
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

(setf (get mobility_topic::Mode :md5sum-) "418c02483a8ca57215fb7b31c5c87234")
(setf (get mobility_topic::Mode :datatype-) "mobility_topic/Mode")
(setf (get mobility_topic::Mode :definition-)
      "int8 mode

")



(provide :mobility_topic/Mode "418c02483a8ca57215fb7b31c5c87234")


