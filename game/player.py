import pygame
import os


MOVE_DICT = {
    pygame.K_a: [-1,0],
    pygame.K_s: [0, 1],
    pygame.K_d: [1, 0],
    pygame.K_w: [0,-1]
    }

class MoveableObject:
    def __init__(self, xPos, yPos, sprite):
        self.xPos, self.yPos = xPos, yPos
        self.sprite = sprite

    def move(self):
        move = MOVE_DICT[key]
        return [self.xPos + move[0], self.yPos + move[1]]

class Timer:
    def __init__(self):
        self.time = 0

if __name__ == '__main__':
    crate_sprite = pygame.image.load(os.path.join('game', 'Assets', 'crate.png'))
    crate = MoveableObject(0, 0, crate_sprite)