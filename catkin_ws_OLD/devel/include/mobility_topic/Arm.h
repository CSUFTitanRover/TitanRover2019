// Generated by gencpp from file mobility_topic/Arm.msg
// DO NOT EDIT!


#ifndef MOBILITY_TOPIC_MESSAGE_ARM_H
#define MOBILITY_TOPIC_MESSAGE_ARM_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mobility_topic
{
template <class ContainerAllocator>
struct Arm_
{
  typedef Arm_<ContainerAllocator> Type;

  Arm_()
    : J1(0)
    , J2(0)
    , J3(0)
    , J4(0)
    , J51(0)
    , J52(0)  {
    }
  Arm_(const ContainerAllocator& _alloc)
    : J1(0)
    , J2(0)
    , J3(0)
    , J4(0)
    , J51(0)
    , J52(0)  {
  (void)_alloc;
    }



   typedef int8_t _J1_type;
  _J1_type J1;

   typedef int8_t _J2_type;
  _J2_type J2;

   typedef int8_t _J3_type;
  _J3_type J3;

   typedef int8_t _J4_type;
  _J4_type J4;

   typedef int8_t _J51_type;
  _J51_type J51;

   typedef int8_t _J52_type;
  _J52_type J52;





  typedef boost::shared_ptr< ::mobility_topic::Arm_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mobility_topic::Arm_<ContainerAllocator> const> ConstPtr;

}; // struct Arm_

typedef ::mobility_topic::Arm_<std::allocator<void> > Arm;

typedef boost::shared_ptr< ::mobility_topic::Arm > ArmPtr;
typedef boost::shared_ptr< ::mobility_topic::Arm const> ArmConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mobility_topic::Arm_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mobility_topic::Arm_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mobility_topic

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'mobility_topic': ['/home/skrapmi/TitanRover2019/catkin_ws/src/mobility_topic/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mobility_topic::Arm_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobility_topic::Arm_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobility_topic::Arm_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobility_topic::Arm_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobility_topic::Arm_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobility_topic::Arm_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mobility_topic::Arm_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9b2ff0d79665aaff197a9e50422410bb";
  }

  static const char* value(const ::mobility_topic::Arm_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9b2ff0d79665aaffULL;
  static const uint64_t static_value2 = 0x197a9e50422410bbULL;
};

template<class ContainerAllocator>
struct DataType< ::mobility_topic::Arm_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mobility_topic/Arm";
  }

  static const char* value(const ::mobility_topic::Arm_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mobility_topic::Arm_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int8 J1\n\
int8 J2\n\
int8 J3\n\
int8 J4\n\
int8 J51\n\
int8 J52\n\
";
  }

  static const char* value(const ::mobility_topic::Arm_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mobility_topic::Arm_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.J1);
      stream.next(m.J2);
      stream.next(m.J3);
      stream.next(m.J4);
      stream.next(m.J51);
      stream.next(m.J52);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Arm_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mobility_topic::Arm_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mobility_topic::Arm_<ContainerAllocator>& v)
  {
    s << indent << "J1: ";
    Printer<int8_t>::stream(s, indent + "  ", v.J1);
    s << indent << "J2: ";
    Printer<int8_t>::stream(s, indent + "  ", v.J2);
    s << indent << "J3: ";
    Printer<int8_t>::stream(s, indent + "  ", v.J3);
    s << indent << "J4: ";
    Printer<int8_t>::stream(s, indent + "  ", v.J4);
    s << indent << "J51: ";
    Printer<int8_t>::stream(s, indent + "  ", v.J51);
    s << indent << "J52: ";
    Printer<int8_t>::stream(s, indent + "  ", v.J52);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOBILITY_TOPIC_MESSAGE_ARM_H
