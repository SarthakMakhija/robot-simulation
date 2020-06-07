from __future__ import annotations

from typing import Tuple, Callable


class Position:

    def __init__(self, value: Tuple[int, int]):
        self.value = value

    def new_position(self, func: Callable[[int, int], Tuple[int, int]]) -> Position:
        x_position, y_position = self.value
        return Position(func(x_position, y_position))

    def __eq__(self, other: Position) -> bool:
        return self.value == other.value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        x_position, y_position = self.value
        return f'Position, x = {x_position} and y = {y_position}'
