from enum import Enum
import os
from game import *
import pygame

WIDTH = 20
HEIGHT = 20
SPRITE_SIZE = 32


class TileType(Enum):
    EMPTY = 1
    WALL = 2
    DEATH = 3
    BORDER = 4
    CRATE = 5


class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4


TILE_DICT = {
    '#': [TileType.WALL, 'wall.png'],
    '_': [TileType.EMPTY, 'empty.png'],
    'X': [TileType.CRATE, 'crate.png'],
    '|': [TileType.BORDER, 'border.png']
}


class Tile:
    def __init__(self, tileType, fileName):
        self.type = tileType


class Environment:
    def __init__(self, path):
        self.height = HEIGHT
        self.width = WIDTH
        self.sprite_size = SPRITE_SIZE
        self.tileMatrix = [[Tile(TileType.WALL, 'wall.png') for i in range(0, self.width)] for x in
                           range(0, self.height)]

        self.openFile(path)

    def openFile(self, path):
        with (open(path)) as file:
            for yIndex, line in enumerate(file):
                for xIndex, ch in enumerate(line):
                    self.tileMatrix[yIndex][xIndex] = Tile(*TILE_DICT[ch])

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.matrix[y][x], end='')
            print()

    def draw(self, winObj):
        for y in range(self.height):
            for x in range(self.width):
                if self.tileTypeMatrix[y][x]:
                    winObj.blit(self.CRATE_IMAGE, (x * self.sprite_size, y * self.sprite_size))

        pygame.display.update()

    #   def identifyField(self, x, y):
    #       return self.tileTypeMatrix[x, y]

    def movePlayer(self):
        print("Todo")

    def checkPlayerMove(self, expX, expY):
        if expX >= self.width | expY >= self.height | self.tileMatrix[expY][expX].type != TileType.EMPTY:
            return
        else:
            Environment.movePlayer()


if __name__ == '__main__':
    env = Environment()
    env.print()
