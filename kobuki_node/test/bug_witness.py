#!/usr/bin/env python

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
    def test_get_yaw_script(self):
        import getYaw
        getYaw.Converter()
        self.assertTrue(True)

    def test_get_odom_2d_script(self):
        import getOdom2D
        getOdom2D.Converter()
        self.assertTrue(True)


if __name__ == "__main__":
    rospack = rospkg.RosPack()
    pkg_path = rospack.get_path("kobuki_node")
    sys.path.append(os.path.join(pkg_path, "scripts"))
    import rosunit
    rosunit.unitrun("kobuki_node", "bug_witness", BugWitness)
