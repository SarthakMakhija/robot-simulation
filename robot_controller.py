from typing import List

from direction import Direction
from position_command import LeftPositionCommand, RightPositionCommand, UpPositionCommand, DownPositionCommand
from robot import Robot


class RobotController:
    def __init__(self, robot: Robot):
        self.__robot = robot

    def move_left(self):
        self.__robot.accept([LeftPositionCommand()])

    def move_right(self):
        self.__robot.accept([RightPositionCommand()])

    def move_up(self):
        self.__robot.accept([UpPositionCommand()])

    def move_down(self):
        self.__robot.accept([DownPositionCommand()])

    def move_robot_in(self, directions: List[Direction]):
        position_commands = []

        for direction in directions:
            if direction == Direction.LEFT:
                position_commands.append(LeftPositionCommand())
            elif direction == Direction.RIGHT:
                position_commands.append(RightPositionCommand())
            elif direction == Direction.UP:
                position_commands.append(UpPositionCommand())
            elif direction == Direction.DOWN:
                position_commands.append(DownPositionCommand())

        self.__robot.accept(position_commands)
