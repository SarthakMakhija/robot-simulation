from unittest import TestCase

from model.position import Position
from command.position_command import LeftPositionCommand, RightPositionCommand, UpPositionCommand, DownPositionCommand


class PositionTest(TestCase):

    def test_left_position(self):
        """
        Creates a position and finds a new position to the left of it
        """
        position_command = LeftPositionCommand()
        new_position = position_command.new_position(from_position=Position((10, 1)))
        self.assertEqual(Position((9, 1)), new_position)

    def test_right_position(self):
        """
        Creates a position and finds a new position to the right of it
        """
        position_command = RightPositionCommand()
        new_position = position_command.new_position(from_position=Position((10, 1)))
        self.assertEqual(Position((11, 1)), new_position)

    def test_up_position(self):
        """
        Creates a position and finds a new position to the up of it
        """
        position_command = UpPositionCommand()
        new_position = position_command.new_position(from_position=Position((10, 1)))
        self.assertEqual(Position((10, 2)), new_position)

    def test_down_position(self):
        """
        Creates a position and finds a new position to the down of it
        """
        position_command = DownPositionCommand()
        new_position = position_command.new_position(from_position=Position((10, 1)))
        self.assertEqual(Position((10, 0)), new_position)
