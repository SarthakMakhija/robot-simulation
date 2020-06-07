from unittest import TestCase

from model.position import Position
from command.position_command import LeftPositionCommand
from model.robot import Robot


class RobotTest(TestCase):

    def test_position_of_robot(self):
        """
        Sets initial position for robot
        """
        robot = Robot(initial_position=Position((10, 1)))
        initial_position = robot.positioned_at()
        self.assertEqual(Position((10, 1)), initial_position)

    def test_robot_accepts_commands_to_change_position(self):
        """
        Robot changes it position based on commands
        """
        robot = Robot(initial_position=Position((10, 1)))
        robot.accept([LeftPositionCommand()])
        self.assertEqual(Position((9, 1)), robot.positioned_at())
