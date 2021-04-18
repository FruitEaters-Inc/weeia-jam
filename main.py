import pygame
import os
from game.environment import *
from pygame import mixer
from game.assets.earDamage import *
from game.assets.brainDamage import *
import random

pygame.font.init()

#CONST
BG_COLOR = (72, 81, 163)
FPS = 60

#GLOBAL
windowsDimensions = (HEIGHT * SPRITE_SIZE), (HEIGHT * SPRITE_SIZE)
WIN = pygame.display.set_mode(windowsDimensions)
pygame.display.set_caption("BrainDamage")

levelList = [
    'intro.txt',
    'level1.txt',
    'level2.txt',
    'level3.txt',
    'level4.txt',
    'level5.txt',
    'level6.txt',
    'level7.txt',
    'level8.txt',
    'level9.txt',
    'level11.txt',
    'finale.txt'
]

#FONT COLORS
WHITE = (255, 255, 255)
CRIMSON = (220, 20, 60)



def playSound(fileName, volume, times):
    sound = pygame.mixer.Sound(os.path.join('game', 'assets', 'music', fileName))
    sound.set_volume(volume)
    sound.play(times)

def printBrainDamage(listOfTexts, fontColor, fontSize, position):
        showText(random.choice(listOfTexts), fontColor, fontSize, position)

        randomize = random.randint(0, 100)
        if randomize > 75:
            playSound(random.choice(earDamage), 1, 0)
        WIN.set_colorkey(CRIMSON)
        pygame.display.update()



def showText(text, color, fontSize, maxPos):
     draw_text = WINNER_FONT.render(text, fontSize, color)
     WIN.blit(draw_text, (random.randint(10, maxPos), random.randint(10, maxPos)))
     pygame.display.update()
     pygame.time.delay(1000)

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

                if key[pygame.K_t]:
                    music.stop()
                    main(levelList.pop(0))

                if key[pygame.K_r]:
                    music.stop()
                    main(level)
                if key[pygame.K_0]:
                    RANDOM_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    printBrainDamage(brainDamage, RANDOM_COLOR, random.randint(1, 5), 300)

                env.movePlayer(key)

            if event.type == LOSE:
                music.stop()
                main(level)
            if event.type == WINNER:
                music.stop()
                main(levelList.pop(0))
                    
        env.draw(WIN)

    pygame.quit()

if __name__ == "__main__":
    main(levelList.pop(0))