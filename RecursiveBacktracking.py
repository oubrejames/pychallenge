import numpy as np
import random

from GenerateMaze import *

NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4


def convert(dir):
    if dir == NORTH: 
        print("NORTH")
    elif dir == EAST: 
        print("EAST")
    elif dir == SOUTH: 
        print("SOUTH")
    elif dir == WEST: 
        print("WEST")


class Solve: 
    def __init__(self, m, n):
        self.mz = Generate(m, n)
        self.history = []
        self.current = self.mz.start
    
    def chooseDirection(self, co): 
        print("Choosing direction:", end='')
        co.p()
        if co.c > 0: 
            if self.mz.maze[co.r][co.c-1] == 0:
                return NORTH
        elif co.r < self.mz.n -1: 
            if self.mz.maze[co.r+1][co.c] == 0:
                return EAST
        elif co.c < self.mz.m - 1: 
            if self.mz.maze[co.r][co.c+1] == 0:
                return SOUTH
        elif co.r > 0: 
            if self.mz.maze[co.r-1][co.c]: 
                return WEST
        else:
            return 0
    
    def moveInDir(self, co, dir):
        if dir == NORTH: 
            return Coord(co.r, co.c-1)
        elif dir == EAST: 
            return Coord(co.r+1, co.c)
        elif dir == SOUTH: 
            return Coord(co.r, co.c+1)
        elif dir == WEST: 
            return Coord(co.r-1, co.c)
        else: 
            return Coord(-1, -1)

    def pop(self):
        # remove and return the most recent addition to the history
        fst = self.history[0]
        self.history = self.history[1:]
        return fst
    def push(self, new):
        # add a placement to the history
        self.history = [new]+self.history
    
    
    def go(self): 
        while not ((self.current.r == self.mz.end.r) and (self.current.c == self.mz.end.c)): 
            print("Current Location:", end='')
            self.current.p()
            direction = self.chooseDirection(self.current)
            convert(direction)
            if direction: 
                print("We can proceed!")
                # we can proceed in some direction
                self.push((direction, self.current))
                self.current = self.moveInDir(self.current, direction)
            else: 
                print("We need to backtrack")
                # Need to backtrack!
                if len(self.history): 
                    last_direction, last_co = self.pop()
                    bad_move = self.moveInDir(last_co, last_direction)
                    # block off the bad move
                    self.mz.maze[bad_move.r][bad_move.c] = 2
                    self.current = last_co
                else: 
                    print("IDK what happened but we can't solve")
                    exit()



        




s = Solve(10, 10)
s.mz.load()
s.go()