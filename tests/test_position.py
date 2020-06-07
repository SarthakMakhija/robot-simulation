from unittest import TestCase

from position import Position


class PositionTest(TestCase):

    def test_new_position(self):
        """
        Creates a position and finds a new position by passing a lambda
        """
        position = Position((10, 1))
        new_position = position.new_position(lambda x, y: (x + 1, y - 2))
        self.assertEqual(Position((11, -1)), new_position)
