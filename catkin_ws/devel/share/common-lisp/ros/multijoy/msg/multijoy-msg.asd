
(cl:in-package :asdf)

(defsystem "multijoy-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "MultiJoy" :depends-on ("_package_MultiJoy"))
    (:file "_package_MultiJoy" :depends-on ("_package"))
  ))