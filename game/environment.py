from enum import Enum
import os
from game import *
import pygame

MOVE_DICT = {
    pygame.K_a: [-1,0],
    pygame.K_s: [0, 1],
    pygame.K_d: [1, 0],
    pygame.K_w: [0,-1]
    }

WIDTH = 20
HEIGHT = 20
SPRITE_SIZE = 32

class TileType(Enum):
    EMPTY = 1
    WALL = 2
    DEATH = 3
    BORDER = 4
    CRATE = 5
    PLAYER = 6



class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4

TILE_DICT = {
    '#': [TileType.WALL, 'crate.png'],
    '_': [TileType.EMPTY, 'empty.png'],
    'X': [TileType.CRATE, 'crate.png'],
    '|': [TileType.BORDER, 'border.png'],
    '@': [TileType.PLAYER, 'chest.png']}


MOVEABLE_TILE = [TileType.CRATE, TileType.PLAYER]
ENTERABLE = [TileType.EMPTY]

class Tile:
    def __init__(self, tileType, fileName):
        self.type = tileType
        self.sprite = pygame.image.load(
            os.path.join('game','assets','textures', fileName))

class Environment:
    def __init__(self, path):
        self.height = HEIGHT
        self.width = WIDTH
        self.sprite_size = SPRITE_SIZE
        self.tileMatrix = [
            [Tile(*TILE_DICT['#']) for i in range(0, self.width)
                ] for x in range(0, self.height)]

        self.openFile(path)

    def openFile(self, path):
        with (open(path)) as f:
            for yIndex, line in enumerate(f):
                for xIndex, ch in enumerate(line):
                    if str(ch) in list(TILE_DICT.keys()):
                        self.tileMatrix[yIndex][xIndex] = Tile(*TILE_DICT[ch])

    def draw(self, winObj):
        for y in range(self.height):
            for x in range(self.width):
                winObj.blit(
                    self.tileMatrix[y][x].sprite, 
                    (x * self.sprite_size, y * self.sprite_size))

        pygame.display.update()

    def getPlayerPosition(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.tileMatrix[y][x].type == TileType.PLAYER:
                    return x, y

    def update(self, srcX, srcY, dstX, dstY):
        src = self.tileMatrix[srcY][srcX]
        dst = self.tileMatrix[dstY][dstX]
        src, dst = dst, src

    def movePlayer(self, keys):
        move = [0, 0]
        if keys[pygame.K_w]:
            move = [0, -1]
        if keys[pygame.K_s]:
            move = [0, 1]
        if keys[pygame.K_a]:
            move = [-1, 0]
        if keys[pygame.K_d]:
            move = [1, 0]
        playerX, playerY = self.getPlayerPosition()
        self.checkMove(playerX, playerX, move)

    def checkMove(self, srcX, srcY, move):
        dstX = srcX + move[0]
        dstY = srcY + move[1]
        if self.tileMatrix[dstY][dstX].type in MOVEABLE_TILE:
            return checkMove(self, dstX, dstY, move)

        if self.tileMatrix[dstY][dstX] in ENTERABLE:
            update(targetX, targetY, expX, expY)
            return True
        return False