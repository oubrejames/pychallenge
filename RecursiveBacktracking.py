import numpy as np
import random

from GenerateMaze import *

NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4


def convert(dir):
    if dir == 1: 
        print("NORTH")
    elif dir == 2: 
        print("EAST")
    elif dir == 3: 
        print("SOUTH")
    elif dir == 4: 
        print("WEST")


class Solve: 
    def __init__(self, m, n):
        self.mz = Generate(m, n)
        self.mz.load()
        self.mz.change_end(1,2)
        self.history = []
        self.current = self.mz.start
    
    def chooseDirection(self, co): 
        print(self.mz.maze)
        if co.c > 0: 
            if self.mz.maze[co.r][co.c-1] == 0:
                print("Allowed North")
                return 1
        if co.r < self.mz.n -1: 
            if self.mz.maze[co.r+1][co.c] == 0:
                print("Allowed East")
                return 2
        if co.c < self.mz.m - 1:
            if self.mz.maze[co.r][co.c+1] == 0:
                print("Allowed South")
                return 3
        if co.r > 0: 
            if self.mz.maze[co.r-1][co.c]: 
                print("Allowed West")
                return 4
        else:
            return 0
    
    def moveInDir(self, co, dir):
        if dir == 1: 
            return Coord(co.r, co.c-1)
        elif dir == 2: 
            return Coord(co.r+1, co.c)
        elif dir == 3: 
            return Coord(co.r, co.c+1)
        elif dir == 4: 
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
        ct = 0
        while not ((self.current.r == self.mz.end.r) and (self.current.c == self.mz.end.c)): 
            ct += 1
            if ct > 50: 
                exit()
            print("Current Location:", end='')
            self.current.p()
            print("End Location:", end='')
            self.mz.end.p()
            if self.current.r == -1 or self.current.c == -1: 
                print("SOMETHING WENT WRONG!!!")
                exit()
            direction = self.chooseDirection(self.current)
            print("Direction:")
            convert(direction)
            if direction is None: 
                print("Why have u forsaken me")
                exit()
            elif direction!=0: 
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
                    print("Blocking off: ", end='')
                    bad_move.p()
                    self.mz.maze[bad_move.r][bad_move.c] = 2
                    self.current = last_co
                else: 
                    print("IDK what happened but we can't solve")
                    exit()
        print("SOLVED:D")



        




s = Solve(10, 10)
s.go()