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

#WINNER EVENT
WINNER = pygame.USEREVENT + 1
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

#LOSE EVENT
LOSE = pygame.USEREVENT + 2
LOSE_FONT = WINNER_FONT

#FONT COLORS
WHITE = (255, 255, 255)
CRIMSON = (220,20,60)

def showText(text, color):
     draw_text = WINNER_FONT.render(text, 1, color)
     WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()) /
              2, HEIGHT/2 - draw_text.get_width()/2)
     pygame.display.update()
     pygame.time.delay(5000)



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