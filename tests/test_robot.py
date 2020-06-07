from typing import Tuple
from unittest import TestCase


class Robot:

    def __init__(self, initial_position: Tuple[int, int]):
        self.__initial_position = initial_position

    def positioned_at(self) -> Tuple[int, int]:
        return self.__initial_position


class RobotTest(TestCase):

    def test_initialize_robot_with_a_sample_initial_position(self):
        """
        Sets initial position for robot
        """
        robot = Robot(initial_position=(10, 1))
        initial_position = robot.positioned_at()
        self.assertEqual((10, 1), initial_position)
