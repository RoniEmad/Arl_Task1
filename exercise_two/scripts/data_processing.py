#!/usr/bin/env python

import rospy
from std_msgs.msg import String,Int64,Float64

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
    name_pub.publish(name)
    age_pub.publish(age)
    height_pub.publish(height)
    print(name)
    print(age)
    print(height)

def subscriber():
    global name_pub
    global age_pub
    global height_pub
    name_pub = rospy.Publisher('name', String, queue_size=10)
    age_pub = rospy.Publisher('age', Int64, queue_size=10)
    height_pub = rospy.Publisher('height', Int64, queue_size=10)
    rospy.init_node('data_processing')
    rospy.Subscriber('raw_data', String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
