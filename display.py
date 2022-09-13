from json import load
import pygame, sys
from pygame.locals import *
import numpy as np
import sys
from GenerateMaze import *
from RecursiveBacktracking import *
from wavefront_planner import *

# Start the game
pygame.init()
clock = pygame.time.Clock()

# Images
tile_img = pygame.image.load("images/tile2.png")
start_img = pygame.image.load("images/start.png")
finish_img = pygame.image.load("images/finish.png")
robot_img = pygame.image.load("images/robot.png")
path_img = pygame.image.load("images/path_img.png")

# Tile Map Properties
M = 20
N = 20
TILE_SZ =  tile_img.get_width() # Hard Coded, will edit to tile.get_width()

# Generate Maze
Maze = Generate(M,N)
game_map = Maze.maze
# Maze.save()
# game_map = Maze.load()
# print("Game map ", game_map)
game_map = game_map.tolist()

# Get Solved Path Coordinates
# TODO: add code for path coordinates casting to list
# Solver for RecursiveBacktracking
Recursive_Solver = Solve(Maze)
# path_coords = Recursive_Solver.go()

Wavefront_Solver = makePath(Maze)
path_coords = Wavefront_Solver.make_map()
path_coords.pop()
path_coords.pop(0)
# print(path_coords)


# Screen Properties 
screen = pygame.display.set_mode((M * TILE_SZ,N * TILE_SZ), 0)
pygame.display.set_caption("a-MAZE-ing Solver!")
BkgdColor = (139, 200, 254)

# Location Information
start_loc = [Maze.start.r, Maze.start.c]
end_loc = [Maze.end.r, Maze.end.c]

# Add location of start and end into the game_map
game_map[start_loc[0]][start_loc[1]] = 2
game_map[end_loc[0]][end_loc[1]] = 3

# Change game_map to a list of strings
game_map = [list(map(str,x)) for x in game_map]

# Change path_coords to a list of ints
# path_coords = [list(map(int,x)) for x in path_coords]
# path_coords = path_coords.tolist()

# Method for adding 1 to every element in the game_map
# test = [list(map(int,x)) for x in game_map]
# test = [[x + 1 for x in y] for y in test]
# print(test)


""" Function - MoveRobot(PathCoords)
    This function updates the game_map to add the little
    robot onto the display screen
"""
def MoveRobot(PathCoords):
    x = PathCoords[0] # Get X and Y of Path
    y = PathCoords[1]

    game_map[x][y] = '5' # Update to path_img

# Booleans
running = True

""" Function - run(loop_num)
    Run's the display, which creates the tile map using game_map
    and also moves the robot from the start to the finish flag
"""
def run(loop_num):
    item = 0
    loop_num = 1
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
                    screen.blit(tile_img, (x * TILE_SZ, y * TILE_SZ)) # Tile
                if tile == '2':
                    screen.blit(start_img, (x * TILE_SZ, y * TILE_SZ)) # Start Flag
                if tile == '3':
                    screen.blit(finish_img, (x * TILE_SZ, y * TILE_SZ)) # End Flag
                # if tile == '4':
                #     screen.blit(path_img, (x * TILE_SZ, y * TILE_SZ))
                if tile == '5':
                    screen.blit(robot_img, (x * TILE_SZ, y * TILE_SZ)) # Little Robot
                if tile != '0':
                    tiles.append(pygame.Rect(x * TILE_SZ, y * TILE_SZ, TILE_SZ, TILE_SZ))
                x += 1 
            y += 1 
        
        # Want to Display the Path only after a set time (1 second delay)
        click_time = pygame.time.get_ticks() / 1000
        go_time = (click_time) % (1 * loop_num)
        # print(click_time, go_time)
            
        if go_time <= 0.01999:
            loop_num += 1
            if item >= len(path_coords) - 1:
                item = len(path_coords) - 1

            MoveRobot(path_coords[item])
            # if item == 0:
            #     prev_loc = path_coords[item]
            #     print(prev_loc)
            item += 1
        
        # Closing the Game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update()
        clock.tick(60) # Run at specified fps

run(1)