from __future__ import annotations

from typing import List

from model.position import Position
from command.position_command import PositionCommand


class Robot:

    def __init__(self, initial_position: Position):
        self.__initial_position = initial_position
        self.__current_position = initial_position

    def positioned_at(self) -> Position:
        return self.__current_position

    def accept(self, position_commands: List[PositionCommand]):
        for command in position_commands:
            self.__current_position = command.new_position(self.__current_position)
