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
def main(level):
    env = Environment(os.path.join('game', 'assets', 'levels', level))
    pygame.init()
    clock = pygame.time.Clock()
    WIN.fill(BG_COLOR)

    # music
    music = pygame.mixer.Sound(os.path.join('game', 'assets', 'music', 'song1.wav'))
    music.set_volume(0.1)
    music.play(-1)

    while True:
        clock.tick(FPS)  # control FPS of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                break
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_r]:
                    music.stop()
                    main(level)
                env.movePlayer(key)
            
                    
        env.draw(WIN)

    pygame.quit()

if __name__ == "__main__":
    main('leveldebug.txt')