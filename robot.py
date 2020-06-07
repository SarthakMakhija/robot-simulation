from __future__ import annotations

from typing import List

from direction import Direction
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

    def move_in(self, directions: List[Direction]) -> Robot:
        for instruction in self.__move_instructions(directions):
            instruction()
        return self

    def __move_instructions(self, directions: List[Direction]):
        instructions = []
        for direction in directions:
            if direction == Direction.LEFT:
                instructions.append(lambda: self.move_left())
        return instructions
