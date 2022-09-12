import pygame, sys
from pygame.locals import *
import numpy as np
import sys
from GenerateMaze import *

# Start the game
pygame.init()
clock = pygame.time.Clock()

# Images
tile_img = pygame.image.load("images/tile.png")
start_img = pygame.image.load("images/start.png")
finish_img = pygame.image.load("images/finish.png")
robot_img = pygame.image.load("images/robot.png")
path_img = pygame.image.load("images/path_img.png")

# Tile Map Properties
M = 20
N = 20
START = 'Some Index'
FINISH = 'Another Index'
TILE_SZ =  tile_img.get_width() # Hard Coded, will edit to tile.get_width()

# Generate Maze
Maze = Generate(M,N)
game_map = Maze.maze
game_map = game_map.tolist()

# Screen Properties 
screen = pygame.display.set_mode((M * TILE_SZ,N * TILE_SZ), 0)
pygame.display.set_caption("a-MAZE-ing Solver!")
BkgdColor = (139, 200, 254)
# ObjectColor = (43, 39, 32)

# Location Information
# robot_loc = [50,50]
start_loc = [Maze.start.r, Maze.start.c]
end_loc = [Maze.end.r, Maze.end.c]
prev_loc = []
item = 0
loop_num = 1



game_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 1, 0], 
            [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], 
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
            [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 3, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

path_coords =[[9,15],[8,15],[7,15],[7,14],[7,13],[7,12],[7,11],[7,10],
              [7,9],[7,8],[7,7],[7,6],[7,5],[6,5],[5,5],[5,4],[5,3],
              [6,3],[7,3],[8,3],[9,3],[10,3],[11,3],[12,3],[13,3],[13,2],[13,1]]


# print(path_coords[2][1])
# Add location of start and end into the game_map
# game_map[start_loc[0]][start_loc[1]] = 2
# game_map[end_loc[0]][end_loc[1]] = 3

# Change game_map to a list of strings
game_map = [list(map(str,x)) for x in game_map]

# Method for adding 1 to every element in the game_map
# test = [list(map(int,x)) for x in game_map]
# test = [[x + 1 for x in y] for y in test]
# print(test)

def MoveRobot(PathCoords):
    x = PathCoords[1] # Get X and Y of Path
    y = PathCoords[0]

    # When I eventually fix the points
    # x = path_coords[i][0] # Get X and Y of Path
    # y = path_coords[i][1]

    game_map[x][y] = '5' # Update to path_img

    # pygame.display.update()


# Booleans
running = True
path_flag = False

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
            # if tile == '4':
            #     screen.blit(path_img, (x * TILE_SZ, y * TILE_SZ))
            if tile == '5':
                screen.blit(robot_img, (x * TILE_SZ, y * TILE_SZ))
            if tile != '0':
                tiles.append(pygame.Rect(x * TILE_SZ, y * TILE_SZ, TILE_SZ, TILE_SZ))
            x += 1 
        y += 1 
    
    # Want to Display the Path only after a set time (1 second delay)
    click_time = pygame.time.get_ticks() / 1000
    go_time = (click_time) % (1 * loop_num)
    # print(click_time, go_time)
        
    if go_time <= 0.01999: # Change hardcoded time delay (currently 5)
        loop_num += 1
        if item >= len(path_coords) - 1:
           item = len(path_coords) - 1

        MoveRobot(path_coords[item])
        if item == 0:
            prev_loc = path_coords[item]
            print(prev_loc)
        item += 1
        
    # screen.blit(robot_img, robot_loc) # Displaying the Robot 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    
    pygame.display.update()
    clock.tick(60) # Run at specified fps