from unittest import TestCase

from robot_controller import RobotController
from direction import Direction
from position import Position
from robot import Robot


class RobotControllerTest(TestCase):
    def test_move_left_twice(self):
        """
        Moves the robot left twice, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot_controller = RobotController(robot=robot)
        robot_controller.move_robot_in([Direction.LEFT, Direction.LEFT])

        self.assertEqual(Position((8, 1)), robot.positioned_at())

    def test_move_left_right_up_followed_by_down_twice(self):
        """
        Moves the robot left right up followed by down twice, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot_controller = RobotController(robot=robot)
        robot_controller.move_robot_in([Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN, Direction.DOWN])

        self.assertEqual(Position((10, 0)), robot.positioned_at())

    def test_move_robot_left(self):
        """
        Moves the robot left, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot_controller = RobotController(robot=robot)
        robot_controller.move_left()

        self.assertEqual(Position((9, 1)), robot.positioned_at())

    def test_move_robot_right(self):
        """
        Moves the robot right, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot_controller = RobotController(robot=robot)
        robot_controller.move_right()

        self.assertEqual(Position((11, 1)), robot.positioned_at())

    def test_move_robot_up(self):
        """
        Moves the robot up, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot_controller = RobotController(robot=robot)
        robot_controller.move_up()

        self.assertEqual(Position((10, 2)), robot.positioned_at())

    def test_move_robot_down(self):
        """
        Moves the robot down, given it has been initialized with a position
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot_controller = RobotController(robot=robot)
        robot_controller.move_down()

        self.assertEqual(Position((10, 0)), robot.positioned_at())
