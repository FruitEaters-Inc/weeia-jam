from enum import Enum
import os
from game import *
import pygame
from pygame import mixer

WIDTH = 20
HEIGHT = 20
SPRITE_SIZE = 32

#WINNER EVENT
pygame.font.init()
WINNER = pygame.USEREVENT + 1
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

#LOSE EVENT
LOSE = pygame.USEREVENT + 2
LOSE_FONT = WINNER_FONT

class TileType(Enum):
    EMPTY = 1
    WALL = 2
    DEATH = 3
    BORDER = 4
    CRATE = 5
    PLAYER = 6
    WALL1 = 7
    SKY = 8
    BIRD = 9
    BRIDGE = 10
    SUITCASE = 11
    DOOR = 12



class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4

TILE_DICT = {
    '#': [TileType.WALL, 'wall1.png'],
    '>': [TileType.BIRD, 'bird.png'],
    '0': [TileType.BIRD, 'sky.png'],
    '$': [TileType.WALL1, 'wall2.png'],
    '_': [TileType.EMPTY, 'empty.png'],
    'X': [TileType.CRATE, 'crate.png'],
    '|': [TileType.BORDER, 'border.png'],
    'S': [TileType.PLAYER, 'spawn.png'],
    'V': [TileType.DEATH, 'hole1.png'],
    'T': [TileType.BRIDGE, 'hole_crate.png'],
    '*': [TileType.SUITCASE, 'suitcase.png'],
    'D': [TileType.DOOR, 'doorUp.png']
    }


MOVEABLE_TILE = [TileType.CRATE, TileType.PLAYER]
ENTERABLE = [TileType.EMPTY, TileType.BRIDGE]

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
        dst = self.tileMatrix[dstY][dstX]
        if dst.type == TileType.BRIDGE:
            dst = Tile(*TILE_DICT['_'])
        src = self.tileMatrix[srcY][srcX]
        self.tileMatrix[srcY][srcX] = dst
        self.tileMatrix[dstY][dstX] = src

    def movePlayer(self, keys):
        move = [0, 0]
        if keys[pygame.K_w]:
            move = [0, -1]
        elif keys[pygame.K_s]:
            move = [0, 1]
        elif keys[pygame.K_a]:
            move = [-1, 0]
        elif keys[pygame.K_d]:
            move = [1, 0]
        elif keys[pygame.K_q]:
            pygame.event.post(pygame.event.Event(QUIT))
            return
        else:
            return
        playerX, playerY = self.getPlayerPosition()
        self.checkMove(playerX, playerY, move)

    def checkMove(self, srcX, srcY, move):
        dstX = srcX + move[0]
        dstY = srcY + move[1]
        if self.tileMatrix[dstY][dstX].type in ENTERABLE:
            self.update(srcX, srcY, dstX, dstY)
            return True
        
        if self.tileMatrix[dstY][dstX].type == TileType.DEATH:
            if self.tileMatrix[srcY][srcX].type == TileType.CRATE:
                self.tileMatrix[srcY][srcX] = Tile(*TILE_DICT['_'])
                self.tileMatrix[dstY][dstX] = Tile(*TILE_DICT['T'])
                return True

            if self.tileMatrix[srcY][srcX].type == TileType.PLAYER:
                pygame.event.post(pygame.event.Event(LOSE))

        if self.tileMatrix[dstY][dstX].type in MOVEABLE_TILE:
            if self.checkMove(dstX, dstY, move):
                self.update(srcX, srcY, dstX, dstY)
                return True
  
        return False