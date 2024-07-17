#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def send_goal():
    rospy.init_node('send_goal')

    pub = rospy.Publisher('/spot/go_to_pose', PoseStamped, queue_size=10)
    rospy.sleep(1) 

    goal = PoseStamped()
    goal.header.frame_id = "body"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 1.00
    goal.pose.position.y = 1.00
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = -0.7 #-0.7   #0.7    #0.0   #-1.0
    goal.pose.orientation.w = 0.7 #0.7     #0.7    #1.0    #0.0

    rospy.loginfo("Sending goal")
    pub.publish(goal)
    rospy.loginfo("Goal sent")

if __name__ == '__main__':
    try:
        send_goal()
    except rospy.ROSInterruptException:
        pass
