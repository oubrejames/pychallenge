import numpy as np
import random

from GenerateMaze import *

class Solve: 
    def __init__(self, m, n):
        self.mz = Generate(m, n)
        self.path = np.zeros((m,n), dtype=int)



Solve(10, 10)