import numpy as np
import random

class Generate: 
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.maze = np.full((m,n),1,dtype=int)
        # Set random cell B to empty
        random_r = random.randrange(0,m)
        random_c = random.randrange(0,n)
        print(random_r, random_c)
        self.maze[random_r][random_c] = 0
        print(self.maze)
        wall_list = self.neighbors(random_r, random_c)
        print(wall_list)
        #while len(wall_list):
        #    wall_c = random.choice(wall_list)
        #    print("WALLC:", wall_c)

        #for r in range(0,m):
        #    for c in range(0,n):
        #        print(self.maze[r][c])
        #        #random.randrange(x,y)

        
        #self.start = (,)
        #self.end = (,)
    def neighbors(self, r, c):
        lst = []
        if r < self.m-1: 
            lst.append((r+1, c))
        if r > 0: 
            lst.append((r-1, c))
        if c < self.n-1: 
            lst.append((r, c+1))
        if c > 0: 
            lst.append((r, c-1))
        return lst

        



Generate(3,8)