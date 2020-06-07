from __future__ import annotations

from typing import Tuple, Callable
from unittest import TestCase


class Position:

    def __init__(self, value: Tuple[int, int]):
        self.__value = value

    def left(self) -> Position:
        return self.__new_position(lambda x_position, y_position: (x_position - 1, y_position))

    def right(self) -> Position:
        return self.__new_position(lambda x_position, y_position: (x_position + 1, y_position))

    def up(self) -> Position:
        return self.__new_position(lambda x_position, y_position: (x_position, y_position + 1))

    def down(self) -> Position:
        return self.__new_position(lambda x_position, y_position: (x_position, y_position - 1))

    def __new_position(self, func: Callable[[int, int], Tuple[int, int]]) -> Position:
        x_position, y_position = self.__value
        return Position(func(x_position, y_position))

    def __eq__(self, other: Position) -> bool:
        return self.__value == other.__value


class Robot:

    def __init__(self, initial_position: Position):
        self.__initial_position = initial_position

    def positioned_at(self) -> Position:
        return self.__initial_position

    def move_left(self) -> Robot:
        self.__initial_position = self.__initial_position.left()
        return self

    def move_right(self):
        self.__initial_position = self.__initial_position.right()
        return self

    def move_up(self):
        self.__initial_position = self.__initial_position.up()
        return self

    def move_down(self):
        self.__initial_position = self.__initial_position.down()
        return self


class RobotTest(TestCase):

    def test_initialize_robot_with_a_sample_initial_position(self):
        """
        Sets initial position for robot
        """
        robot = Robot(initial_position=Position((10, 1)))
        initial_position = robot.positioned_at()
        self.assertEqual(Position((10, 1)), initial_position)

    def test_move_robot_left(self):
        """
        Moves the robot left, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot.move_left()
        self.assertEqual(Position((9, 1)), robot.positioned_at())

    def test_move_robot_right(self):
        """
        Moves the robot right, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot.move_right()
        self.assertEqual(Position((11, 1)), robot.positioned_at())

    def test_move_robot_up(self):
        """
        Moves the robot up, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot.move_up()
        self.assertEqual(Position((10, 2)), robot.positioned_at())

    def test_move_robot_down(self):
        """
        Moves the robot down, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot.move_down()
        self.assertEqual(Position((10, 0)), robot.positioned_at())
