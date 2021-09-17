#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from exercise_three.msg import UserInfo

global name
global age
global height

def callback(data):
    my_list=data.data.replace(" ","")
    my_list=my_list.replace(":",",")
    my_list=my_list.split(",")
    msg = UserInfo()
    msg.name=my_list[1]
    msg.age=int(my_list[3])
    msg.height=int(my_list[5])
    pub.publish(msg)
    print(msg)

def subscriber():
    print("data_processing.py")
    global pub
    pub = rospy.Publisher('user_info', UserInfo, queue_size=10)
    rospy.init_node('data_processing')
    rospy.Subscriber('raw_data', String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
