import pygame

MOVE_PLAYER = {
    pygame.K_a: [-1,0],
    pygame.K_s: [0, 1],
    pygame.K_d: [1, 0],
    pygame.K_w: [0,-1]
    }

class Player:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def move(self, key):
        move = MOVE_PLAYER[key]
        return [self.xPos + move[0], self.yPos + move[1]]
        
class Timer:
    def __init__(self):
        self.time = 0

if __name__ == '__main__':
    player = Player(0, 0)
    print(player.move(pygame.K_a))