// Auto-generated. Do not edit!

// (in-package test_mobility.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Mobility = require('./Mobility.js');
let Arm = require('./Arm.js');
let Mode = require('./Mode.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class joystick {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.mobility = null;
      this.arm = null;
      this.mode = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('mobility')) {
        this.mobility = initObj.mobility
      }
      else {
        this.mobility = new Mobility();
      }
      if (initObj.hasOwnProperty('arm')) {
        this.arm = initObj.arm
      }
      else {
        this.arm = new Arm();
      }
      if (initObj.hasOwnProperty('mode')) {
        this.mode = initObj.mode
      }
      else {
        this.mode = new Mode();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type joystick
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [mobility]
    bufferOffset = Mobility.serialize(obj.mobility, buffer, bufferOffset);
    // Serialize message field [arm]
    bufferOffset = Arm.serialize(obj.arm, buffer, bufferOffset);
    // Serialize message field [mode]
    bufferOffset = Mode.serialize(obj.mode, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type joystick
    let len;
    let data = new joystick(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [mobility]
    data.mobility = Mobility.deserialize(buffer, bufferOffset);
    // Deserialize message field [arm]
    data.arm = Arm.deserialize(buffer, bufferOffset);
    // Deserialize message field [mode]
    data.mode = Mode.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'test_mobility/joystick';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ed6711036913a5609081e2c7ac5cd927';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    MSG: test_mobility/Mobility
    int8 ForwardY
    int8 TurningX
    
    ================================================================================
    MSG: test_mobility/Arm
    int8 J1
    int8 J2
    int8 J3
    int8 J4
    int8 J51
    int8 J52
    
    ================================================================================
    MSG: test_mobility/Mode
    int8 mode
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new joystick(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.mobility !== undefined) {
      resolved.mobility = Mobility.Resolve(msg.mobility)
    }
    else {
      resolved.mobility = new Mobility()
    }

    if (msg.arm !== undefined) {
      resolved.arm = Arm.Resolve(msg.arm)
    }
    else {
      resolved.arm = new Arm()
    }

    if (msg.mode !== undefined) {
      resolved.mode = Mode.Resolve(msg.mode)
    }
    else {
      resolved.mode = new Mode()
    }

    return resolved;
    }
};

module.exports = joystick;
