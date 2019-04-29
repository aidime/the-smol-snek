import numpy as np

class Snek:

        def __init__(self):
                self.name = "snek"
                self.x = 0
                self.y = 0
                self.length = 1
                self.orientation = 0
                self.orientation_dict = {0 : "up", 1 : "right", 2 : "down", 3 : "left"}

def forward(self):
        if self.orientation == 0:
                self.y += 1
        if self.orientation == 2:
                self.y -= 1
        if self.orientation == 3:
                self.x -= 1
        if self.orientation == 1:
                self.x += 1

def turn_left(self):
        self.orientation = (self.orientation - 1)%4

def turn_right(self):
        self.orientation = (self.orientation + 1)%4

def feed(self):
        self.length += 1


