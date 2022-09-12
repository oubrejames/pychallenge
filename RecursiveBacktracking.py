import numpy as np
import random

from GenerateMaze import *

NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

class Solve: 
    def __init__(self, m, n):
        self.mz = Generate(m, n)
        self.history = []
        self.current = self.mz.start
    
    def move(self, co): 
        if co.c > 0: 
            if self.mz.maze[co.r][co.c-1] == 0:
                return (NORTH, Coord(co.r, co.c-1)) 
        elif co.r < self.mz.n -1: 
            if self.mz.maze[co.r+1][co.c] == 0:
                return (EAST, Coord(co.r+1, co.c)) 
        elif co.c < self.mz.m - 1: 
            if self.mz.maze[co.r][co.c+1] == 0:
                return (SOUTH, Coord(co.r, co.c+1)) 
        elif co.r > 0: 
            if self.mz.maze[co.r-1][co.c]: 
                return (WEST, Coord(co.r-1, co.c)) 
        else:
            return (0, Coord(-1, -1))

    def pop(self):
        # remove and return the most recent addition to the history
        fst = self.history[0]
        self.history = self.history[1:]
        return fst
    def push(self, new):
        # add a placement to the history
        self.history = [new]+self.history
    
    
    def go(self): 
        while (self.current.r != self.mz.end.r) and (self.current.c != self.mz.end.c): 
            print("Current Location:", end='')
            self.current.p()
            direction, co = self.move(self.current)
            co.p()
            print(direction)
            if direction: 
                print("We can proceed!")
                # we can proceed in some direction
                self.push((direction, co))
                self.current = co
            else: 
                print("NEEDD to backtrack")
                # Need to backtrack!
                last_direction, last_co = self.pop()


        




s = Solve(10, 10)
s.go()