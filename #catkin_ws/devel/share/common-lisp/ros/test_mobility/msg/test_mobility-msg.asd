
(cl:in-package :asdf)

(defsystem "test_mobility-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Arm" :depends-on ("_package_Arm"))
    (:file "_package_Arm" :depends-on ("_package"))
    (:file "Mobility" :depends-on ("_package_Mobility"))
    (:file "_package_Mobility" :depends-on ("_package"))
    (:file "Mode" :depends-on ("_package_Mode"))
    (:file "_package_Mode" :depends-on ("_package"))
    (:file "joystick" :depends-on ("_package_joystick"))
    (:file "_package_joystick" :depends-on ("_package"))
  ))