// Generated by gencpp from file test_mobility/Mode.msg
// DO NOT EDIT!


#ifndef TEST_MOBILITY_MESSAGE_MODE_H
#define TEST_MOBILITY_MESSAGE_MODE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace test_mobility
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





  typedef boost::shared_ptr< ::test_mobility::Mode_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_mobility::Mode_<ContainerAllocator> const> ConstPtr;

}; // struct Mode_

typedef ::test_mobility::Mode_<std::allocator<void> > Mode;

typedef boost::shared_ptr< ::test_mobility::Mode > ModePtr;
typedef boost::shared_ptr< ::test_mobility::Mode const> ModeConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_mobility::Mode_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_mobility::Mode_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace test_mobility

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'test_mobility': ['/home/nvidia/catkin_ws/src/test_mobility/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::test_mobility::Mode_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_mobility::Mode_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_mobility::Mode_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_mobility::Mode_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_mobility::Mode_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_mobility::Mode_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_mobility::Mode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "418c02483a8ca57215fb7b31c5c87234";
  }

  static const char* value(const ::test_mobility::Mode_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x418c02483a8ca572ULL;
  static const uint64_t static_value2 = 0x15fb7b31c5c87234ULL;
};

template<class ContainerAllocator>
struct DataType< ::test_mobility::Mode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_mobility/Mode";
  }

  static const char* value(const ::test_mobility::Mode_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_mobility::Mode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int8 mode\n\
";
  }

  static const char* value(const ::test_mobility::Mode_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_mobility::Mode_<ContainerAllocator> >
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
struct Printer< ::test_mobility::Mode_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test_mobility::Mode_<ContainerAllocator>& v)
  {
    s << indent << "mode: ";
    Printer<int8_t>::stream(s, indent + "  ", v.mode);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_MOBILITY_MESSAGE_MODE_H
