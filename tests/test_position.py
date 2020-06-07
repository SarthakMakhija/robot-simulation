from unittest import TestCase

from position import Position


class PositionTest(TestCase):

    def test_left_position(self):
        """
        Creates a position and finds a new position to the left of it
        """
        position = Position((10, 1))
        left_position = position.left()
        self.assertEqual(Position((9, 1)), left_position)

    def test_right_position(self):
        """
        Creates a position and finds a new position to the right of it
        """
        position = Position((10, 1))
        right_position = position.right()
        self.assertEqual(Position((11, 1)), right_position)

    def test_up_position(self):
        """
        Creates a position and finds a new position to the up of it
        """
        position = Position((10, 1))
        up_position = position.up()
        self.assertEqual(Position((10, 2)), up_position)

    def test_down_position(self):
        """
        Creates a position and finds a new position to the down of it
        """
        position = Position((10, 1))
        down_position = position.down()
        self.assertEqual(Position((10, 0)), down_position)
