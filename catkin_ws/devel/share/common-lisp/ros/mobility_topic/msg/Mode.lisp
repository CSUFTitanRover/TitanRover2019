; Auto-generated. Do not edit!


(cl:in-package mobility_topic-msg)


;//! \htmlinclude Mode.msg.html

(cl:defclass <Mode> (roslisp-msg-protocol:ros-message)
  ((mode
    :reader mode
    :initarg :mode
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Mode (<Mode>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Mode>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Mode)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mobility_topic-msg:<Mode> is deprecated: use mobility_topic-msg:Mode instead.")))

(cl:ensure-generic-function 'mode-val :lambda-list '(m))
(cl:defmethod mode-val ((m <Mode>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobility_topic-msg:mode-val is deprecated.  Use mobility_topic-msg:mode instead.")
  (mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Mode>) ostream)
  "Serializes a message object of type '<Mode>"
  (cl:let* ((signed (cl:slot-value msg 'mode)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Mode>) istream)
  "Deserializes a message object of type '<Mode>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mode) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Mode>)))
  "Returns string type for a message object of type '<Mode>"
  "mobility_topic/Mode")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Mode)))
  "Returns string type for a message object of type 'Mode"
  "mobility_topic/Mode")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Mode>)))
  "Returns md5sum for a message object of type '<Mode>"
  "418c02483a8ca57215fb7b31c5c87234")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Mode)))
  "Returns md5sum for a message object of type 'Mode"
  "418c02483a8ca57215fb7b31c5c87234")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Mode>)))
  "Returns full string definition for message of type '<Mode>"
  (cl:format cl:nil "int8 mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Mode)))
  "Returns full string definition for message of type 'Mode"
  (cl:format cl:nil "int8 mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Mode>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Mode>))
  "Converts a ROS message object to a list"
  (cl:list 'Mode
    (cl:cons ':mode (mode msg))
))
