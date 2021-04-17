import pygame
import os
from game.environment import *
from pygame import mixer

#CONST
BG_COLOR = (72, 81, 163)
FPS = 60

#GLOBAL
windowsDimensions = (HEIGHT * SPRITE_SIZE), (HEIGHT * SPRITE_SIZE)
WIN = pygame.display.set_mode(windowsDimensions)
pygame.display.set_caption("MindHacker")

# main window
def main():
    env = Environment(os.path.join('game','assets','levels','leveldebug.txt'))
    pygame.init()
    clock = pygame.time.Clock()
    WIN.fill(BG_COLOR)

    # music
    music = pygame.mixer.Sound(os.path.join('game', 'assets', 'music', 'song1.wav'))
    music.set_volume(0.1)
    music.play(-1)

    run = True
    while run:
        clock.tick(FPS)  # control FPS of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                env.movePlayer(key)
                    
        env.draw(WIN)

    pygame.quit()

if __name__ == "__main__":
    main()