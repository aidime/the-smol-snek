try:
    import tkinter as tk  # assume Python 3
except ImportError:
    import Tkinter as tk  # nope, Python 2

class Board:    

        def __init__(self, height, width):

                self.height = height
                self.width = width
                self.tiles = makeTiles(height, width)

        class Tile:
                def __init__(self, x, y, color, isOccupied):
                        self.x = x
                        self.y = y
                        self.color = color
                        self.isOccupied = isOccupied

def makeBoard(height, width):
                board = Board(height, width)
                return board    

def makeTiles(height, width):
                tiles = [[Board.Tile(x, y, "lightgray", False) for x in range(width)] for y in range(height)]
                return tiles