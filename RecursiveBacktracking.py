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
    def __init__(self, mz):
        self.mz = mz
        self.history = []
        self.on_path = []
        self.current = self.mz.start
    
    def chooseDirection(self, co): 
        if co.r > 0: 
            if (self.mz.maze[co.r-1][co.c] == 0) and (co.r-1, co.c) not in self.on_path:
                print("Allowed North")
                return 1
        if co.c < self.mz.n - 1: 
            if (self.mz.maze[co.r][co.c+1] == 0) and (co.r, co.c+1) not in self.on_path:
                print("Allowed East")
                return 2
        if co.r < self.mz.m - 1:
            if (self.mz.maze[co.r+1][co.c] == 0) and (co.r+1, co.c) not in self.on_path:
                print("Allowed South")
                return 3
        if co.c > 0: 
            if (self.mz.maze[co.r][co.c-1] == 0) and (co.r, co.c-1) not in self.on_path: 
                print("Allowed West")
                return 4
        return 0
    
    def moveInDir(self, co, dir):
        if dir == 1: 
            # NORTH
            return Coord(co.r-1, co.c)
        elif dir == 2: 
            # EAST
            return Coord(co.r, co.c+1)
        elif dir == 3: 
            # SOUTH
            return Coord(co.r+1, co.c)
        elif dir == 4: 
            # WEST
            return Coord(co.r, co.c-1)
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
            print("Current Location: ", end='')
            self.current.p()
            if self.current.r == -1 or self.current.c == -1: 
                print("SOMETHING WENT WRONG!!!")
                exit()
            current_tuple = (self.current.r, self.current.c)
            if current_tuple not in self.on_path:
                self.on_path.append(current_tuple)
            direction = self.chooseDirection(self.current)
            if direction is None: 
                print("why are u doing this the direction should never be none")
                exit()
            elif direction!=0: 
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
                    print("Blocking off + removing from path: ", end='')
                    bad_move.p()
                    self.mz.maze[bad_move.r][bad_move.c] = 2
                    self.on_path.remove((bad_move.r, bad_move.c))
                    self.current = last_co
                else: 
                    print("IDK what happened but we can't solve")
                    exit()
        print()
        print("SOLVED :D")
        print("Start: ", end='')
        self.mz.start.p()
        print("End: ", end='')
        self.mz.end.p()
        print("Path:", end='')
        self.on_path.append((self.mz.end.r, self.mz.end.c))
        print(self.on_path)
        self.mz.maze[self.mz.maze == 2] = 0
        return self.on_path

