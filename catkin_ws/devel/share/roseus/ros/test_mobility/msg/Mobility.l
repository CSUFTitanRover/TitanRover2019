;; Auto-generated. Do not edit!


(when (boundp 'test_mobility::Mobility)
  (if (not (find-package "TEST_MOBILITY"))
    (make-package "TEST_MOBILITY"))
  (shadow 'Mobility (find-package "TEST_MOBILITY")))
(unless (find-package "TEST_MOBILITY::MOBILITY")
  (make-package "TEST_MOBILITY::MOBILITY"))

(in-package "ROS")
;;//! \htmlinclude Mobility.msg.html


(defclass test_mobility::Mobility
  :super ros::object
  :slots (_ForwardY _TurningX ))

(defmethod test_mobility::Mobility
  (:init
   (&key
    ((:ForwardY __ForwardY) 0)
    ((:TurningX __TurningX) 0)
    )
   (send-super :init)
   (setq _ForwardY (round __ForwardY))
   (setq _TurningX (round __TurningX))
   self)
  (:ForwardY
   (&optional __ForwardY)
   (if __ForwardY (setq _ForwardY __ForwardY)) _ForwardY)
  (:TurningX
   (&optional __TurningX)
   (if __TurningX (setq _TurningX __TurningX)) _TurningX)
  (:serialization-length
   ()
   (+
    ;; int8 _ForwardY
    1
    ;; int8 _TurningX
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _ForwardY
       (write-byte _ForwardY s)
     ;; int8 _TurningX
       (write-byte _TurningX s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _ForwardY
     (setq _ForwardY (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _ForwardY 127) (setq _ForwardY (- _ForwardY 256)))
   ;; int8 _TurningX
     (setq _TurningX (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _TurningX 127) (setq _TurningX (- _TurningX 256)))
   ;;
   self)
  )

(setf (get test_mobility::Mobility :md5sum-) "80c0a058aa7119b3181b6edb07201e22")
(setf (get test_mobility::Mobility :datatype-) "test_mobility/Mobility")
(setf (get test_mobility::Mobility :definition-)
      "int8 ForwardY
int8 TurningX

")



(provide :test_mobility/Mobility "80c0a058aa7119b3181b6edb07201e22")

