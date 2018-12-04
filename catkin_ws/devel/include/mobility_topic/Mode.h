// Generated by gencpp from file mobility_topic/Mode.msg
// DO NOT EDIT!


#ifndef MOBILITY_TOPIC_MESSAGE_MODE_H
#define MOBILITY_TOPIC_MESSAGE_MODE_H


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
struct Mode_
{
  typedef Mode_<ContainerAllocator> Type;

  Mode_()
    : mode(0)  {
    }
  Mode_(const ContainerAllocator& _alloc)
    : mode(0)  {
  (void)_alloc;
    }



   typedef int8_t _mode_type;
  _mode_type mode;





  typedef boost::shared_ptr< ::mobility_topic::Mode_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mobility_topic::Mode_<ContainerAllocator> const> ConstPtr;

}; // struct Mode_

typedef ::mobility_topic::Mode_<std::allocator<void> > Mode;

typedef boost::shared_ptr< ::mobility_topic::Mode > ModePtr;
typedef boost::shared_ptr< ::mobility_topic::Mode const> ModeConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mobility_topic::Mode_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mobility_topic::Mode_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mobility_topic

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'mobility_topic': ['/home/nvidia/catkin_ws/src/mobility_topic/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mobility_topic::Mode_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobility_topic::Mode_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobility_topic::Mode_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobility_topic::Mode_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobility_topic::Mode_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobility_topic::Mode_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mobility_topic::Mode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "418c02483a8ca57215fb7b31c5c87234";
  }

  static const char* value(const ::mobility_topic::Mode_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x418c02483a8ca572ULL;
  static const uint64_t static_value2 = 0x15fb7b31c5c87234ULL;
};

template<class ContainerAllocator>
struct DataType< ::mobility_topic::Mode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mobility_topic/Mode";
  }

  static const char* value(const ::mobility_topic::Mode_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mobility_topic::Mode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int8 mode\n\
";
  }

  static const char* value(const ::mobility_topic::Mode_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mobility_topic::Mode_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.mode);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Mode_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mobility_topic::Mode_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mobility_topic::Mode_<ContainerAllocator>& v)
  {
    s << indent << "mode: ";
    Printer<int8_t>::stream(s, indent + "  ", v.mode);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOBILITY_TOPIC_MESSAGE_MODE_H
