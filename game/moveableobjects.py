import pygame
import os

MOVE_DICT = {
    pygame.K_a: [-1,0],
    pygame.K_s: [0, 1],
    pygame.K_d: [1, 0],
    pygame.K_w: [0,-1]
    }

class MoveableObject():
    def __init__(self, xPos, yPos):
        self.xPos, self.yPos = xPos, yPos

    def move(self):
        move = MOVE_DICT[key]
        return [self.xPos + move[0], self.yPos + move[1]]