from __future__ import annotations

from typing import List

from position import Position
from position_command import PositionCommand


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

    def accept(self, position_commands: List[PositionCommand]):
        for command in position_commands:
            self.__initial_position = command.new_position(self.__initial_position)
