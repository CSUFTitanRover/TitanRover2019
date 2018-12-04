// Auto-generated. Do not edit!

// (in-package test_mobility.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Mobility {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ForwardY = null;
      this.TurningX = null;
    }
    else {
      if (initObj.hasOwnProperty('ForwardY')) {
        this.ForwardY = initObj.ForwardY
      }
      else {
        this.ForwardY = 0;
      }
      if (initObj.hasOwnProperty('TurningX')) {
        this.TurningX = initObj.TurningX
      }
      else {
        this.TurningX = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Mobility
    // Serialize message field [ForwardY]
    bufferOffset = _serializer.int8(obj.ForwardY, buffer, bufferOffset);
    // Serialize message field [TurningX]
    bufferOffset = _serializer.int8(obj.TurningX, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Mobility
    let len;
    let data = new Mobility(null);
    // Deserialize message field [ForwardY]
    data.ForwardY = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [TurningX]
    data.TurningX = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 2;
  }

  static datatype() {
    // Returns string type for a message object
    return 'test_mobility/Mobility';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '80c0a058aa7119b3181b6edb07201e22';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 ForwardY
    int8 TurningX
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Mobility(null);
    if (msg.ForwardY !== undefined) {
      resolved.ForwardY = msg.ForwardY;
    }
    else {
      resolved.ForwardY = 0
    }

    if (msg.TurningX !== undefined) {
      resolved.TurningX = msg.TurningX;
    }
    else {
      resolved.TurningX = 0
    }

    return resolved;
    }
};

module.exports = Mobility;
