from __future__ import annotations
from position import Position


class Robot:

    def __init__(self, initial_position: Position):
        self.__initial_position = initial_position

    def positioned_at(self) -> Position:
        return self.__initial_position

    def move_left(self) -> Robot:
        self.__initial_position = self.__initial_position.left()
        return self

    def move_right(self) -> Robot:
        self.__initial_position = self.__initial_position.right()
        return self

    def move_up(self) -> Robot:
        self.__initial_position = self.__initial_position.up()
        return self

    def move_down(self) -> Robot:
        self.__initial_position = self.__initial_position.down()
        return self
