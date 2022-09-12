

class Wavefront_Planner:
    """Implementing the wavefront planner algorithm"""
    
    def __init__(self, M, N, maze, start, goal):
        self.M = M
        self.N = N
        self.maze = maze
        self.start = start
        self.goal = goal
        
    def find_path(self):
        path = []
        current_pos = [self.start[0], self.start[1]]
        path.append(current_pos[:])
        while (current_pos != self.goal):
            