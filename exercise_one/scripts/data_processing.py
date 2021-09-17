#!/usr/bin/env python

import rospy
from std_msgs.msg import String

global name
global age
global height

def callback(data):
    my_list=data.data.replace(" ","")
    my_list=my_list.replace(":",",")
    my_list=my_list.split(",")
    name=my_list[1]
    age=int(my_list[3])
    height=int(my_list[5])
    print(name)
    print(age)
    print(height)

def subscriber():
    rospy.init_node('data_processing')
    rospy.Subscriber('raw_data', String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
