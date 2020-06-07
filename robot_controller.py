from direction import Direction
from position_command import LeftPositionCommand, RightPositionCommand, UpPositionCommand, DownPositionCommand
from robot import Robot


class RobotController:
    def __init__(self, robot: Robot):
        self.__robot = robot

    def move_robot_in(self, directions: [Direction]):
        position_commands = []

        for direction in directions:
            if direction == Direction.LEFT:
                position_commands.append(LeftPositionCommand())
            if direction == Direction.RIGHT:
                position_commands.append(RightPositionCommand())
            if direction == Direction.UP:
                position_commands.append(UpPositionCommand())
            if direction == Direction.DOWN:
                position_commands.append(DownPositionCommand())

        self.__robot.accept(position_commands)
