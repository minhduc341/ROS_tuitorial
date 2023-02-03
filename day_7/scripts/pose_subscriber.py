#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_calback(msg: Pose):
    rospy.loginfo("(" + str(msg.x) + "," + str(msg.y) + ")")

if __name__ == '__main__':
    rospy.init_node("turtle_pose_subcriber")
    
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_calback)

    rospy.loginfo("Node has been started")

    rospy.spin() #block until node is killed
