from typing import List

from model.direction import Direction
from command.position_command import LeftPositionCommand, RightPositionCommand, UpPositionCommand, DownPositionCommand
from model.robot import Robot


class RobotController:
    def __init__(self, robot: Robot):
        self.__robot = robot
        self.__command_by_direction = {
            Direction.LEFT: LeftPositionCommand(),
            Direction.RIGHT: RightPositionCommand(),
            Direction.UP: UpPositionCommand(),
            Direction.DOWN: DownPositionCommand()
        }

    def move_left(self):
        self.__robot.accept([LeftPositionCommand()])

    def move_right(self):
        self.__robot.accept([RightPositionCommand()])

    def move_up(self):
        self.__robot.accept([UpPositionCommand()])

    def move_down(self):
        self.__robot.accept([DownPositionCommand()])

    def move_robot_in(self, directions: List[Direction]):
        position_commands = [self.__command_by_direction[direction] for direction in directions]
        self.__robot.accept(position_commands)
