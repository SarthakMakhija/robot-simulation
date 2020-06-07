from abc import ABC, abstractmethod

from model.position import Position


class PositionCommand(ABC):
    @abstractmethod
    def new_position(self, from_position: Position):
        pass


class LeftPositionCommand(PositionCommand):
    def new_position(self, from_position: Position):
        return from_position.new_position(lambda x_position, y_position: (x_position - 1, y_position))


class RightPositionCommand(PositionCommand):
    def new_position(self, from_position: Position):
        return from_position.new_position(lambda x_position, y_position: (x_position + 1, y_position))


class UpPositionCommand(PositionCommand):
    def new_position(self, from_position: Position):
        return from_position.new_position(lambda x_position, y_position: (x_position, y_position + 1))


class DownPositionCommand(PositionCommand):
    def new_position(self, from_position: Position):
        return from_position.new_position(lambda x_position, y_position: (x_position, y_position - 1))
