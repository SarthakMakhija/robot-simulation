from unittest import TestCase

from direction import Direction
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

    def test_move_left_twice(self):
        """
        Moves the robot left twice, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot.move_in(directions=[Direction.LEFT, Direction.LEFT])
        self.assertEqual(Position((8, 1)), robot.positioned_at())
