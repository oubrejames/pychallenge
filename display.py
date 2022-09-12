import pygame, sys
from pygame.locals import *
import numpy as np
import sys

# Start the game
pygame.init()
clock = pygame.time.Clock()

# Images
tile_img = pygame.image.load("images/tile.png")
start_img = pygame.image.load("images/start.png")
finish_img = pygame.image.load("images/finish.png")
robot_img = pygame.image.load("images/robot.png")

# Tile Map Properties
M = 20
N = 20
START = 'Some Index'
FINISH = 'Another Index'
TILE_SZ =  tile_img.get_width() # Hard Coded, will edit to tile.get_width()

# Screen Properties 
screen = pygame.display.set_mode((M * TILE_SZ,N * TILE_SZ), 0)
pygame.display.set_caption("a-MAZE-ing Solver!")
BkgdColor = (139, 200, 254)
# ObjectColor = (43, 39, 32)

# Player Information
robot_loc = [50,50]

# Numpy Conversion
# nparray.tolist()


# Game Map
game_map = [['2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','3']]

# Booleans
running = True

# Game Loop
while running:
    screen.fill(BkgdColor) # Fill the Display with chosen background 

    # Displaying Game Map
    tiles = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                screen.blit(tile_img, (x * TILE_SZ, y * TILE_SZ))
            if tile == '2':
                screen.blit(start_img, (x * TILE_SZ, y * TILE_SZ))
            if tile == '3':
                screen.blit(finish_img, (x * TILE_SZ, y * TILE_SZ))
            if tile != '0':
                tiles.append(pygame.Rect(x * TILE_SZ, y * TILE_SZ, TILE_SZ, TILE_SZ))
            x += 1 
        y += 1 
        
    screen.blit(robot_img, robot_loc) # Displaying the Robot 

    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60) # Run at specified fps
