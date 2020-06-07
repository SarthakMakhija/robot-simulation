from __future__ import annotations
from typing import Tuple
from unittest import TestCase


class Robot:

    def __init__(self, initial_position: Tuple[int, int]):
        self.__initial_position = initial_position

    def positioned_at(self) -> Tuple[int, int]:
        return self.__initial_position

    def move_left(self) -> Robot:
        x_position, y_position = self.__initial_position
        self.__initial_position = (x_position - 1, y_position)
        return self


class RobotTest(TestCase):

    def test_initialize_robot_with_a_sample_initial_position(self):
        """
        Sets initial position for robot
        """
        robot = Robot(initial_position=(10, 1))
        initial_position = robot.positioned_at()
        self.assertEqual((10, 1), initial_position)

    def test_move_robot_left(self):
        """
        Moves the robot left, given it has been initialized with a position
        """
        robot = Robot(initial_position=(10, 1))
        robot.move_left()
        self.assertEqual((9, 1), robot.positioned_at())
