import pygame
import os

# lets make a new window that takes our width and height
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MindHacker")

BG_COLOR = (72, 81, 163)

FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
PLAYER_X, PLAYER_Y = 100, 300
VEL = 10

PLAYER_IMAGE = pygame.image.load(
    os.path.join('Assets', 'Sprite1.png'))
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

def drawWindow(playerHitbox):
    # drawing a background here

    WIN.fill(BG_COLOR)
    WIN.blit(PLAYER, (playerHitbox.x, playerHitbox.y))
    pygame.display.update()



def movePlayer(keys_pressed, player):
    if keys_pressed[pygame.K_a]:  # LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_d]:  # RIGHT
        player.x += VEL
    if keys_pressed[pygame.K_w]:  # UP
        player.y -= VEL
    if keys_pressed[pygame.K_s]:  # DOWN
        player.y += VEL


# main window
def main():

    playerHitbox = pygame.Rect(150, 150, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)  # control FPS of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()
        movePlayer(keys_pressed, playerHitbox)
        drawWindow(playerHitbox)

    pygame.quit()


if __name__ == "__main__":
    main()
