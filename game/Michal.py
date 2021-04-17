import pygame

# lets make a new window that takes our width and height
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MindHacker")

BG_COLOR = (72, 81, 163)

FPS = 60


def drawWindow():
    # drawing a background here
    WIN.fill(BG_COLOR)
    pygame.display.update()


# main window
def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)  # control FPS of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawWindow()

    pygame.quit()


if __name__ == "__main__":
    main()
