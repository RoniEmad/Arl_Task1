#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('raw_data', String, queue_size=10)
    rospy.init_node('user_info_driver')
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        my_str = "name: Rose, age: 20, height:170"
        rospy.loginfo(my_str)
        pub.publish(my_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
