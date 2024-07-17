#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler

def send_goal(x, y, theta):
    pub = rospy.Publisher('/spot/go_to_pose', PoseStamped, queue_size=10)
    rospy.sleep(1) 

    goal = PoseStamped()
    goal.header.frame_id = "body"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.position.z = 0.0

    # Convert the Euler angle (theta) to quaternion
    quat = quaternion_from_euler(0.0, 0.0, theta)
    goal.pose.orientation.x = quat[0]
    goal.pose.orientation.y = quat[1]
    goal.pose.orientation.z = quat[2]
    goal.pose.orientation.w = quat[3]

    rospy.loginfo("Sending goal")
    pub.publish(goal)
    rospy.loginfo("Goal sent")

if __name__ == '__main__':
    try:
        rospy.init_node('send_goal')

        goals = [
            (6.0, 0.0, 0.0),   
            (0.0, 2.0, 0.0),    
            (-6.0, 0.0, 0.0),
            (0.0, -2.0, 0.0)  
        ]

        for x, y, theta in goals:
            send_goal(x, y, theta)
            rospy.sleep(6)

    except rospy.ROSInterruptException:
        pass
