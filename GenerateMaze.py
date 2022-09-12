import numpy as np
import random


class Coord:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def p(self):
        print(f"{self.r}, {self.c}")

def print_coord_list(l):
    for c in l: 
        c.p()

class Generate: 
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.maze = np.full((m,n),1,dtype=int)
        # Set random cell B to empty
        random_r = random.randrange(0,m)
        random_c = random.randrange(0,n)
        cell_b = Coord(random_r, random_c)
        cell_b.p()
        self.maze[random_r][random_c] = 0
        print(self.maze)
        wall_list = self.neighbors(cell_b)
        while len(wall_list):
            print_coord_list(wall_list)
            wall_c = random.choice(wall_list)
            wall_c.p()
            #find the cell A that wall C divides
            if cell_b.r == wall_c.r: 
                print("Same row")
                if cell_b.c > wall_c.c: 
                    print("Decrease col")
                    new_c = wall_c.c - 1
                    print(new_c)
                else: 
                    print("Increase col")
                    new_c = wall_c.c + 1
                    print(new_c)
                cell_a = Coord(cell_b.r, new_c)
            elif cell_b.c == wall_c.c:
                print("Same col")
                if cell_b.r > wall_c.r: 
                    print("Decrease row")
                    new_r = wall_c.r - 1
                    print(new_r)
                else: 
                    print("Increase row")
                    new_r = wall_c.r + 1
                    print(new_r)
                cell_a = Coord(new_r, cell_b.c)
            # IF cell_A is a wall (code 1)
            if (self.maze[cell_a.r][cell_a.c]):
                # Make cell D whichever one is the wall
                cell_d = cell_a
                #Free Cell C
                self.maze[wall_c.r][wall_c.c] = 0
                #Free Cell D
                self.maze[cell_d.r][cell_d.c] = 0
                #Not sure about this one...
                cell_b = cell_d
                wall_list += self.neighbors(cell_d)
            elif (self.maze[cell_b.r][cell_b.c]):
                # Make cell D whichever one is the wall
                cell_d = cell_b
                #Free Cell C
                self.maze[wall_c.r][wall_c.c] = 0
                #Free Cell D
                self.maze[cell_d.r][cell_d.c] = 0
                #Not sure about this one...
                cell_b = cell_d
                wall_list += self.neighbors(cell_d)
            wall_list.remove(wall_c)
            print(self.maze)
            #exit()

        #self.start = (,)
        #self.end = (,)

    #Now this only returns neighbors that are walls. 
    def neighbors(self, co):
        lst = []
        if co.r < self.m-1: 
            nb = Coord(co.r+1, co.c)
            if self.maze[nb.r][nb.c]:
                lst.append(nb)
        if co.r > 0: 
            nb = Coord(co.r-1, co.c)
            if self.maze[nb.r][nb.c]:
                lst.append(nb)
        if co.c < self.n-1: 
            nb = Coord(co.r, co.c+1)
            if self.maze[nb.r][nb.c]:
                lst.append(nb)
        if co.c > 0: 
            nb = Coord(co.r, co.c-1)
            if self.maze[nb.r][nb.c]:
                lst.append(nb)
        return lst

        



Generate(3,8)