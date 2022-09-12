from importlib.resources import path
from GenerateMaze import *
"""Implementing the wavefront planner algorithm"""

class makePath:
    def __init__(self):
        self.maze = Generate(10,10)
        self.maze.load()
        self.cnt = 1
        self.path_map = np.full(self.maze.maze.shape, 999)
        self.stage_list = []

    def make_map(self):
        print('Start ')
        self.maze.start.p()
        print('End ')
        self.maze.end.p()
        
        self.path_map[self.maze.start.r][self.maze.start.c] = 0
        self.path_map[self.maze.end.r][self.maze.end.c] = 222

        self.loop_squares()
        print(self.path_map)
        print_coord_list(self.stage_list)
        #self.check_surround()

    def are_we_there_yet(self, point):
        if point.r == self.maze.end.r and point.c == self.maze.end.c:
            return True
        else: 
            return False

    def check_surround(self, point):
        # Check bottom
        # If point is not on bottom
        self.stage_list.clear()
        if point.r < self.maze.m-1:
            below_contents = self.maze.maze[point.r+1][point.c]
            
            if below_contents == 1: # Is there obstacle
                pass
            elif below_contents == 0 and self.path_map[point.r+1][point.c] == 999: # If free, add label
                self.path_map[point.r+1][point.c] = self.cnt
                self.stage_list.append(Coord(point.r+1,point.c))
                print("Added ", self.cnt, " to stage list for below")

        # Check above
        if point.r < 0:
            above_contents = self.maze.maze[point.r-1][point.c]
            
            if above_contents == 1: # Is there obstacle
                pass
            elif above_contents == 0 and self.path_map[point.r-1][point.c] == 999: # If free, add label
                self.path_map[point.r-1][point.c] = self.cnt
                self.stage_list.append(Coord(point.r-1,point.c))
                print("Added ", self.cnt, " to stage list for above")

        # Check Right
        if point.c < self.maze.n-1:
            right_contents = self.maze.maze[point.r][point.c+1]
            if right_contents == 1: # Is there obstacle
                pass
            elif right_contents == 0 and self.path_map[point.r][point.c+1] == 999: # If free, add label
                self.path_map[point.r][point.c+1] = self.cnt
                self.stage_list.append(Coord(point.r,point.c+1))
                print("Added ", self.cnt, " to stage list for right")

        # Check left
        if point.c < 0:
            left_contents = self.maze.maze[[point.r],[point.c-1]]
            if left_contents == 1: # Is there obstacle
                pass
            elif left_contents == 0 and self.path_map[point.r][point.c-1] == 999: # If free, add label
                self.path_map[point.r][point.c-1] = self.cnt
                self.stage_list.append(Coord(point.r,point.c-1))
                print("Added ", self.cnt, " to stage list for left")
    
    def loop_squares(self):
        
        self.check_surround(self.maze.start)

        print("FHFJHFHFHF")
        print_coord_list(self.stage_list)
        flag = True

        while not flag:
            tmp_stage = self.stage_list
            for i in tmp_stage:
                self.check_surround(i)
                flag = are_we_there_yet(i)
                #i.p()
                
            self.cnt += 1

    




def main():
    """Main"""
    temp = makePath()
    temp.make_map()
    

if __name__ == "__main__":
    main()