import pygame
import os
from game.environment import *


env = Environment()
# lets make a new window that takes our width and height
HEIGHT, WIDTH = (env.height * env.sprite_size), (env.width * env.sprite_size)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MindHacker")

BG_COLOR = (72, 81, 163)

FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
PLAYER_X, PLAYER_Y = 100, 300
VEL = 10

def drawWindow():
    # drawing a background here

    WIN.fill(BG_COLOR)
    env.draw(WIN)

# main window
def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)  # control FPS of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()
        drawWindow()

    pygame.quit()


if __name__ == "__main__":
    main()
