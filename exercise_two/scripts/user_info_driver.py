#!/usr/bin/env python
import rospy
from std_msgs.msg import String

global name
global age
global height

def publisher():
    pub = rospy.Publisher('raw_data', String, queue_size=10)
    rospy.init_node('user_info_driver')
    rate = rospy.Rate(1)
    name = input("Name: ")
    age = input("Age: ")
    height = input("Height: ")
    while not rospy.is_shutdown():
    	my_str = "name: "+ name +", age: "+age+", height:"+height
    	rospy.loginfo(my_str)
    	pub.publish(my_str)
    	rate.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
