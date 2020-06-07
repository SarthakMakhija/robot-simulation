from unittest import TestCase

from position import Position
from robot import Robot


class RobotTest(TestCase):

    def test_initialize_robot_with_a_sample_initial_position(self):
        """
        Sets initial position for robot
        """
        robot = Robot(initial_position=Position((10, 1)))
        initial_position = robot.positioned_at()
        self.assertEqual(Position((10, 1)), initial_position)
