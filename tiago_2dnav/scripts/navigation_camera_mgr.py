#!/usr/bin/env python
import rospy
from actionlib_msgs.msg import GoalStatusArray
from control_msgs.msg import PointHeadActionGoal

class NavigationCameraMgr:

    def __init__(self):
        self.previous_status = None

        rospy.Subscriber('move_base/status', 
            GoalStatusArray, self.callback)
        self.pub_head_topic = rospy.Publisher(
            '/head_controller/point_head_action/goal', 
            PointHeadActionGoal, queue_size=1)

        rospy.loginfo("monitoring move_base goal " 
            "status and moving the head accordingly.")

    def look_down(self):
        phag = PointHeadActionGoal()
        phag.header.frame_id = "/base_link"
        phag.goal.max_velocity = 1.0
        phag.goal.min_duration = rospy.Duration(0.2)

        phag.goal.target.header.frame_id = "/base_link"
        phag.goal.target.point.x = 0.9

        phag.goal.pointing_axis.x = 1.0
        phag.goal.pointing_frame = "/head_2_link"

        self.pub_head_topic.publish(phag)

    def look_up(self):    
        phag = PointHeadActionGoal()
        phag.header.frame_id = "/base_link"
        phag.goal.max_velocity = 1.0
        phag.goal.min_duration = rospy.Duration(0.2)

        phag.goal.target.header.frame_id = "/base_link"
        phag.goal.target.point.x = 0.9
        phag.goal.target.point.z = 1.0

        phag.goal.pointing_axis.x = 1.0
        phag.goal.pointing_frame = "/head_2_link"

        self.pub_head_topic.publish(phag)

    def callback(self, data):
        if not data.status_list:
            return

        self.goal = data.status_list.pop()

        if (self.goal.status == 1 and 
            self.goal.status != self.previous_status):
            self.look_down()
            rospy.loginfo(self.goal.text)

        elif (self.goal.status != 1 and 
            self.goal.status != self.previous_status):
            self.look_up()
            rospy.loginfo(self.goal.text)

        self.previous_status = self.goal.status

    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            # self.pub_head_topic.publish(phag)
            r.sleep()
        
if __name__ == '__main__':
    rospy.init_node('mb_status')
    mb_status = NavigationCameraMgr()
    mb_status.run()