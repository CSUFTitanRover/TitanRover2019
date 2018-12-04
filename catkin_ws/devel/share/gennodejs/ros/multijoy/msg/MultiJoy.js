// Auto-generated. Do not edit!

// (in-package multijoy.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let sensor_msgs = _finder('sensor_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class MultiJoy {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.njoys = null;
      this.joys = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('njoys')) {
        this.njoys = initObj.njoys
      }
      else {
        this.njoys = new std_msgs.msg.UInt8();
      }
      if (initObj.hasOwnProperty('joys')) {
        this.joys = initObj.joys
      }
      else {
        this.joys = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MultiJoy
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [njoys]
    bufferOffset = std_msgs.msg.UInt8.serialize(obj.njoys, buffer, bufferOffset);
    // Serialize message field [joys]
    // Serialize the length for message field [joys]
    bufferOffset = _serializer.uint32(obj.joys.length, buffer, bufferOffset);
    obj.joys.forEach((val) => {
      bufferOffset = sensor_msgs.msg.Joy.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MultiJoy
    let len;
    let data = new MultiJoy(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [njoys]
    data.njoys = std_msgs.msg.UInt8.deserialize(buffer, bufferOffset);
    // Deserialize message field [joys]
    // Deserialize array length for message field [joys]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.joys = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.joys[i] = sensor_msgs.msg.Joy.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.joys.forEach((val) => {
      length += sensor_msgs.msg.Joy.getMessageSize(val);
    });
    return length + 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'multijoy/MultiJoy';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd1fe0e1be06cf2ea74daadf46387e623';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    std_msgs/UInt8 njoys
    sensor_msgs/Joy[] joys
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
    MSG: std_msgs/UInt8
    uint8 data
    
    ================================================================================
    MSG: sensor_msgs/Joy
    # Reports the state of a joysticks axes and buttons.
    Header header           # timestamp in the header is the time the data is received from the joystick
    float32[] axes          # the axes measurements from a joystick
    int32[] buttons         # the buttons measurements from a joystick 
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MultiJoy(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.njoys !== undefined) {
      resolved.njoys = std_msgs.msg.UInt8.Resolve(msg.njoys)
    }
    else {
      resolved.njoys = new std_msgs.msg.UInt8()
    }

    if (msg.joys !== undefined) {
      resolved.joys = new Array(msg.joys.length);
      for (let i = 0; i < resolved.joys.length; ++i) {
        resolved.joys[i] = sensor_msgs.msg.Joy.Resolve(msg.joys[i]);
      }
    }
    else {
      resolved.joys = []
    }

    return resolved;
    }
};

module.exports = MultiJoy;
