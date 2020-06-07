from abc import ABC, abstractmethod

from position import Position


class PositionCommand(ABC):
    @abstractmethod
    def new_position(self, from_position: Position):
        pass


class LeftPositionCommand(PositionCommand):
    def new_position(self, from_position: Position):
        return from_position.left()


class RightPositionCommand(PositionCommand):
    def new_position(self, from_position: Position):
        return from_position.right()


class UpPositionCommand(PositionCommand):
    def new_position(self, from_position: Position):
        return from_position.up()


class DownPositionCommand(PositionCommand):
    def new_position(self, from_position: Position):
        return from_position.down()
