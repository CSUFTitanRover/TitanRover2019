; Auto-generated. Do not edit!


(cl:in-package mobility_topic-msg)


;//! \htmlinclude Mobility.msg.html

(cl:defclass <Mobility> (roslisp-msg-protocol:ros-message)
  ((ForwardY
    :reader ForwardY
    :initarg :ForwardY
    :type cl:fixnum
    :initform 0)
   (TurningX
    :reader TurningX
    :initarg :TurningX
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Mobility (<Mobility>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Mobility>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Mobility)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mobility_topic-msg:<Mobility> is deprecated: use mobility_topic-msg:Mobility instead.")))

(cl:ensure-generic-function 'ForwardY-val :lambda-list '(m))
(cl:defmethod ForwardY-val ((m <Mobility>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobility_topic-msg:ForwardY-val is deprecated.  Use mobility_topic-msg:ForwardY instead.")
  (ForwardY m))

(cl:ensure-generic-function 'TurningX-val :lambda-list '(m))
(cl:defmethod TurningX-val ((m <Mobility>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobility_topic-msg:TurningX-val is deprecated.  Use mobility_topic-msg:TurningX instead.")
  (TurningX m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Mobility>) ostream)
  "Serializes a message object of type '<Mobility>"
  (cl:let* ((signed (cl:slot-value msg 'ForwardY)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'TurningX)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Mobility>) istream)
  "Deserializes a message object of type '<Mobility>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ForwardY) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'TurningX) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Mobility>)))
  "Returns string type for a message object of type '<Mobility>"
  "mobility_topic/Mobility")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Mobility)))
  "Returns string type for a message object of type 'Mobility"
  "mobility_topic/Mobility")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Mobility>)))
  "Returns md5sum for a message object of type '<Mobility>"
  "80c0a058aa7119b3181b6edb07201e22")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Mobility)))
  "Returns md5sum for a message object of type 'Mobility"
  "80c0a058aa7119b3181b6edb07201e22")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Mobility>)))
  "Returns full string definition for message of type '<Mobility>"
  (cl:format cl:nil "int8 ForwardY~%int8 TurningX~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Mobility)))
  "Returns full string definition for message of type 'Mobility"
  (cl:format cl:nil "int8 ForwardY~%int8 TurningX~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Mobility>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Mobility>))
  "Converts a ROS message object to a list"
  (cl:list 'Mobility
    (cl:cons ':ForwardY (ForwardY msg))
    (cl:cons ':TurningX (TurningX msg))
))
