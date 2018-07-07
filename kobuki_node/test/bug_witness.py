#!/usr/bin/env python

import imp
import os
import sys
import unittest

import rospy
import rospkg

################################################################################
# Necessary Overrides
################################################################################

def mock_rospy_init(name, anonymous=False):
    pass

rospy.init_node = mock_rospy_init

class MockSubscriber(object):
    def __init__(self, topic, msg, callback):
        pass

rospy.Subscriber = MockSubscriber

class MockPublisher(object):
    def __init__(self, topic, msg_class, queue_size=None):
        if queue_size is None:
            raise ValueError("Queue size should not be None.")

rospy.Publisher = MockPublisher


################################################################################
# Unit Test
################################################################################

class BugWitness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rospack = rospkg.RosPack()
        pkg_path = rospack.get_path("kobuki_node")
        scripts = os.path.join(pkg_path, "scripts")
        cls.getYaw_py = imp.load_source("getYaw",
                                os.path.join(scripts, "getYaw.py"))
        cls.getOdom2D_py = imp.load_source("getOdom2D",
                                os.path.join(scripts, "getOdom2D.py"))

    def test_get_yaw_script(self):
        self.getYaw_py.Converter()
        self.assertTrue(True)

    def test_get_odom_2d_script(self):
        self.getOdom2D_py.Converter()
        self.assertTrue(True)


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun("kobuki_node", "bug_witness", BugWitness)
