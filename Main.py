import sys

import pygame

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class cSnek:
    class Segment:
        def __init__(self, Gameboard):
            self.Gameboard = Gameboard

class cGameboard:
    def __init__(self, Surface, TileWidth, TileHeight):
        self.Surface = Surface
        self.TileWidth = TileWidth
        self.TileHeight = TileHeight

    def FillTile(self, pos, color):
        Surface.fill(pygame.Rect(pos.x / self.TileWidth, pos.y / self.TileHeight, self.TileWidth, self.TileHeight), color)

def main()
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Snek Game")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

main()