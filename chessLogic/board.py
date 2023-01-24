MAX_WIDTH = 8
MAX_HEIGHT = 8

class Board():
    """A class for the chess board"""
    def __init__(self):
        self.width = MAX_WIDTH
        self.height = MAX_HEIGHT
        self.grid = [[None for item in range(self.height)] for other in range(self.height)]
        self.potentialMove = [[None for item in range(self.height)] for other in range(self.width)]
        