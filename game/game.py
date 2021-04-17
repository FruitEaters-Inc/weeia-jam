from enum import Enum
from game import *


class TileType(Enum):
    EMPTY = 1
    WALL = 2
    DEATH = 3
    BORDER = 4

class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4


class Environment:
    def __init__(self):
        self.height = 30
        self.width = 30
        self.sprite_size = 32
        self.matrix = [['#' for i in range(0, self.width)] for x in range(0, self.height)]
        self.tileTypeMatrix = [[1 for i in range(0, self.width)] for x in range(0, self.height)]
    
    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.matrix[y][x], end='')
            print()

 #   def identifyField(self, x, y):
 #       return self.tileTypeMatrix[x, y]

    def movePlayer(self):
        print("Todo")


    def checkPlayerMove(self, expX, expY):
        if expX >= self.width | expY >= self.height | self.tileTypeMatrix[expY][expX] != TileType.EMPTY:
            return
        else:
            Environment.movePlayer()




if __name__ == '__main__':
    env = Environment()
    env.print()