class Player:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    def move(self):
        print(sys.stdin.read(1))



class Timer:
    def __init__(self):
        self.time = 0

if __name__ == '__main__':
    player = Player(0, 0)
    player.move()