// Generated by gencpp from file mobility_topic/joystick.msg
// DO NOT EDIT!


#ifndef MOBILITY_TOPIC_MESSAGE_JOYSTICK_H
#define MOBILITY_TOPIC_MESSAGE_JOYSTICK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <mobility_topic/Mobility.h>
#include <mobility_topic/Arm.h>
#include <mobility_topic/Mode.h>

namespace mobility_topic
{
template <class ContainerAllocator>
struct joystick_
{
  typedef joystick_<ContainerAllocator> Type;

  joystick_()
    : header()
    , mobility()
    , arm()
    , mode()  {
    }
  joystick_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , mobility(_alloc)
    , arm(_alloc)
    , mode(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::mobility_topic::Mobility_<ContainerAllocator>  _mobility_type;
  _mobility_type mobility;

   typedef  ::mobility_topic::Arm_<ContainerAllocator>  _arm_type;
  _arm_type arm;

   typedef  ::mobility_topic::Mode_<ContainerAllocator>  _mode_type;
  _mode_type mode;





  typedef boost::shared_ptr< ::mobility_topic::joystick_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mobility_topic::joystick_<ContainerAllocator> const> ConstPtr;

}; // struct joystick_

typedef ::mobility_topic::joystick_<std::allocator<void> > joystick;

typedef boost::shared_ptr< ::mobility_topic::joystick > joystickPtr;
typedef boost::shared_ptr< ::mobility_topic::joystick const> joystickConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mobility_topic::joystick_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mobility_topic::joystick_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mobility_topic

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'mobility_topic': ['/home/skrapmi/TitanRover2019/catkin_ws/src/mobility_topic/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mobility_topic::joystick_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobility_topic::joystick_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobility_topic::joystick_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobility_topic::joystick_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobility_topic::joystick_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobility_topic::joystick_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mobility_topic::joystick_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ed6711036913a5609081e2c7ac5cd927";
  }

  static const char* value(const ::mobility_topic::joystick_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xed6711036913a560ULL;
  static const uint64_t static_value2 = 0x9081e2c7ac5cd927ULL;
};

template<class ContainerAllocator>
struct DataType< ::mobility_topic::joystick_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mobility_topic/joystick";
  }

  static const char* value(const ::mobility_topic::joystick_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mobility_topic::joystick_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
Mobility mobility\n\
Arm arm\n\
Mode mode\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: mobility_topic/Mobility\n\
int8 ForwardY\n\
int8 TurningX\n\
\n\
================================================================================\n\
MSG: mobility_topic/Arm\n\
int8 J1\n\
int8 J2\n\
int8 J3\n\
int8 J4\n\
int8 J51\n\
int8 J52\n\
\n\
================================================================================\n\
MSG: mobility_topic/Mode\n\
int8 mode\n\
";
  }

  static const char* value(const ::mobility_topic::joystick_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mobility_topic::joystick_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.mobility);
      stream.next(m.arm);
      stream.next(m.mode);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct joystick_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mobility_topic::joystick_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mobility_topic::joystick_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "mobility: ";
    s << std::endl;
    Printer< ::mobility_topic::Mobility_<ContainerAllocator> >::stream(s, indent + "  ", v.mobility);
    s << indent << "arm: ";
    s << std::endl;
    Printer< ::mobility_topic::Arm_<ContainerAllocator> >::stream(s, indent + "  ", v.arm);
    s << indent << "mode: ";
    s << std::endl;
    Printer< ::mobility_topic::Mode_<ContainerAllocator> >::stream(s, indent + "  ", v.mode);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOBILITY_TOPIC_MESSAGE_JOYSTICK_H