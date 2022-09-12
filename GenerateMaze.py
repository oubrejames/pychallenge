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
        #cell_b.p()
        self.maze[random_r][random_c] = 0
        #print(self.maze)
        wall_list = self.neighbors(cell_b)
        empty_cells = [cell_b]
        while len(wall_list):
            wall_c = random.choice(wall_list)
            #wall_c.p()
            #print("CELL B")
            cell_b = self.free_neighbors(wall_c)[0]
            #cell_b.p()
            #find the cell A that wall C divides
            if cell_b.r == wall_c.r: 
                #print("Same row")
                if cell_b.c > wall_c.c: 
                    #print("Decrease col")
                    new_c = wall_c.c - 1
                    #print(new_c)
                else: 
                    #print("Increase col")
                    new_c = wall_c.c + 1
                    #print(new_c)
                if new_c < self.n and new_c >= 0: 
                    cell_a = Coord(cell_b.r, new_c)
                else: 
                    wall_list.remove(wall_c)
                    #print("OUT OF RANGE")
                    continue
            elif cell_b.c == wall_c.c:
                #print("Same col")
                if cell_b.r > wall_c.r: 
                    #print("Decrease row")
                    new_r = wall_c.r - 1
                    #print(new_r)
                else: 
                    #print("Increase row")
                    new_r = wall_c.r + 1
                    #print(new_r)
                if new_r < self.m and new_r >= 0: 
                    cell_a = Coord(new_r, cell_b.c)
                else: 
                    wall_list.remove(wall_c)
                    #print("OUT OF RANGE")
                    continue
            # IF cell_A is a wall (code 1)
            #SHOULD ALWAYS BE THE CASE: 
            if (self.maze[cell_a.r][cell_a.c]):
                # Make cell D whichever one is the wall
                cell_d = cell_a
                #Free Cell C
                self.maze[wall_c.r][wall_c.c] = 0
                empty_cells.append(wall_c)
                #Free Cell D
                self.maze[cell_d.r][cell_d.c] = 0
                empty_cells.append(cell_d)

                wall_list += self.neighbors(cell_d)
            else:
                #print("A is already empty!!!!!")
                pass
            wall_list.remove(wall_c)
            #print(self.maze)
            #print()

        self.start = random.choice(empty_cells)
        self.end = random.choice(empty_cells)
        while self.end == self.start: 
            self.end = random.choice(empty_cells)
        print(f"Size: {self.m}x{self.n}")
        print(f"Start: ({self.start.r},{self.start.c})")
        print(f"End: ({self.end.r},{self.end.c})")
        print("MAZE:")
        self.print_maze()

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
    def free_neighbors(self, co):
        lst = []
        if co.r < self.m-1: 
            nb = Coord(co.r+1, co.c)
            if not self.maze[nb.r][nb.c]:
                lst.append(nb)
        if co.r > 0: 
            nb = Coord(co.r-1, co.c)
            if not self.maze[nb.r][nb.c]:
                lst.append(nb)
        if co.c < self.n-1: 
            nb = Coord(co.r, co.c+1)
            if not self.maze[nb.r][nb.c]:
                lst.append(nb)
        if co.c > 0: 
            nb = Coord(co.r, co.c-1)
            if not self.maze[nb.r][nb.c]:
                lst.append(nb)
        return lst
    def print_maze(self):
        for c in range(0, self.n):
                print("-",end='')
        print('--') 
        for r in range(0, self.m):
            print("|",end='')
            for c in range(0, self.n):
                if self.maze[r][c]:
                    print("X",end='')
                else: 
                    print(" ",end='')
            print("|")
        for c in range(0, self.n):
            print("-",end='')
        print('--')
    def save(self):
        f = open('maze.txt', 'w')
        f.write(str(self.m)+'\n')
        f.write(str(self.n)+'\n')
        f.write(str(self.start.r)+' '+str(self.start.c)+'\n')
        f.write(str(self.end.r)+' '+str(self.end.c)+'\n')
        for r in range(0, self.m):
            f.write(str(self.maze[r]).strip('[]')+'\n')
        f.close()
    def load(self):
        f = open('maze.txt', 'r')
        lines = f.readlines()
        self.m = int(lines[0])
        self.n = int(lines[1])
        spl_start = (lines[2]).split()
        self.start = Coord(int(spl_start[0]), int(spl_start[1]))
        spl_end = (lines[3]).split()
        self.end = Coord(int(spl_end[0]), int(spl_start[1]))
        nlines = len(lines)
        final = []
        for l in range(4, nlines):
            lst = list(int(i) for i in lines[l].split())
            final.append(lst)
        self.maze = np.array(final)
        self.print_maze()
        f.close()