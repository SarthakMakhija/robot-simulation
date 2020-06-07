from __future__ import annotations
from typing import Tuple, Callable


class Position:

    def __init__(self, value: Tuple[int, int]):
        self.__value = value

    def left(self) -> Position:
        return self.__new_position(lambda x_position, y_position: (x_position - 1, y_position))

    def right(self) -> Position:
        return self.__new_position(lambda x_position, y_position: (x_position + 1, y_position))

    def up(self) -> Position:
        return self.__new_position(lambda x_position, y_position: (x_position, y_position + 1))

    def down(self) -> Position:
        return self.__new_position(lambda x_position, y_position: (x_position, y_position - 1))

    def __new_position(self, func: Callable[[int, int], Tuple[int, int]]) -> Position:
        x_position, y_position = self.__value
        return Position(func(x_position, y_position))

    def __eq__(self, other: Position) -> bool:
        return self.__value == other.__value
