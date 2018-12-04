; Auto-generated. Do not edit!


(cl:in-package test_topic-msg)


;//! \htmlinclude Arm.msg.html

(cl:defclass <Arm> (roslisp-msg-protocol:ros-message)
  ((J1
    :reader J1
    :initarg :J1
    :type cl:fixnum
    :initform 0)
   (J2
    :reader J2
    :initarg :J2
    :type cl:fixnum
    :initform 0)
   (J3
    :reader J3
    :initarg :J3
    :type cl:fixnum
    :initform 0)
   (J4
    :reader J4
    :initarg :J4
    :type cl:fixnum
    :initform 0)
   (J51
    :reader J51
    :initarg :J51
    :type cl:fixnum
    :initform 0)
   (J52
    :reader J52
    :initarg :J52
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Arm (<Arm>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Arm>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Arm)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test_topic-msg:<Arm> is deprecated: use test_topic-msg:Arm instead.")))

(cl:ensure-generic-function 'J1-val :lambda-list '(m))
(cl:defmethod J1-val ((m <Arm>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_topic-msg:J1-val is deprecated.  Use test_topic-msg:J1 instead.")
  (J1 m))

(cl:ensure-generic-function 'J2-val :lambda-list '(m))
(cl:defmethod J2-val ((m <Arm>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_topic-msg:J2-val is deprecated.  Use test_topic-msg:J2 instead.")
  (J2 m))

(cl:ensure-generic-function 'J3-val :lambda-list '(m))
(cl:defmethod J3-val ((m <Arm>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_topic-msg:J3-val is deprecated.  Use test_topic-msg:J3 instead.")
  (J3 m))

(cl:ensure-generic-function 'J4-val :lambda-list '(m))
(cl:defmethod J4-val ((m <Arm>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_topic-msg:J4-val is deprecated.  Use test_topic-msg:J4 instead.")
  (J4 m))

(cl:ensure-generic-function 'J51-val :lambda-list '(m))
(cl:defmethod J51-val ((m <Arm>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_topic-msg:J51-val is deprecated.  Use test_topic-msg:J51 instead.")
  (J51 m))

(cl:ensure-generic-function 'J52-val :lambda-list '(m))
(cl:defmethod J52-val ((m <Arm>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_topic-msg:J52-val is deprecated.  Use test_topic-msg:J52 instead.")
  (J52 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Arm>) ostream)
  "Serializes a message object of type '<Arm>"
  (cl:let* ((signed (cl:slot-value msg 'J1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'J2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'J3)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'J4)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'J51)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'J52)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Arm>) istream)
  "Deserializes a message object of type '<Arm>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'J1) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'J2) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'J3) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'J4) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'J51) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'J52) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Arm>)))
  "Returns string type for a message object of type '<Arm>"
  "test_topic/Arm")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Arm)))
  "Returns string type for a message object of type 'Arm"
  "test_topic/Arm")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Arm>)))
  "Returns md5sum for a message object of type '<Arm>"
  "9b2ff0d79665aaff197a9e50422410bb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Arm)))
  "Returns md5sum for a message object of type 'Arm"
  "9b2ff0d79665aaff197a9e50422410bb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Arm>)))
  "Returns full string definition for message of type '<Arm>"
  (cl:format cl:nil "int8 J1~%int8 J2~%int8 J3~%int8 J4~%int8 J51~%int8 J52~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Arm)))
  "Returns full string definition for message of type 'Arm"
  (cl:format cl:nil "int8 J1~%int8 J2~%int8 J3~%int8 J4~%int8 J51~%int8 J52~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Arm>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Arm>))
  "Converts a ROS message object to a list"
  (cl:list 'Arm
    (cl:cons ':J1 (J1 msg))
    (cl:cons ':J2 (J2 msg))
    (cl:cons ':J3 (J3 msg))
    (cl:cons ':J4 (J4 msg))
    (cl:cons ':J51 (J51 msg))
    (cl:cons ':J52 (J52 msg))
))
