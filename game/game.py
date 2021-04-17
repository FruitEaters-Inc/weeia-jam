
class Environment:
    def __init__(self):
        self.height = 30
        self.width = 60
        self.matrix = [['#' for i in range(0, self.width)] for x in range(0, self.height)]
    
    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.matrix[y][x], end='')
            print()

if __name__ == '__main__':
    env = Environment()
    env.print()