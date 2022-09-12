from importlib.resources import path
from GenerateMaze import *
"""Implementing the wavefront planner algorithm"""

class makePath:
    def __init__(self):
        self.maze = Generate(10,10)
        self.cnt = 1
        self.path_map = np.full(self.maze.maze.shape, 999)
        self.stage_list = []
        self.savior = True

    def make_map(self):
        print('Start ')
        self.maze.start.p()
        print('End ')
        self.maze.end.p()
        
        self.path_map[self.maze.start.r][self.maze.start.c] = 0

        self.loop_squares()
        print(self.path_map)
        #self.check_surround()

    def check_surround(self, point):
        # Check bottom
        # If point is not on bottom
        if point.r < self.maze.m-1:
            below_contents = self.maze.maze[point.r+1][point.c]
            
            if below_contents == 1: # Is there obstacle
                pass
            elif below_contents == 0 and self.path_map[point.r+1][point.c] == 999: # If free, add label
                self.path_map[point.r+1][point.c] = self.cnt
                self.stage_list.append(Coord(point.r+1,point.c))

                #print("Coord: ", point.r+1, "Maze end ", self.maze.end.r)

                #if Coord(point.r+1,point.c) == self.maze.end:
                if point.r== self.maze.end.r and point.c == self.maze.end.c:
                    print("HERE")
                    self.savior = False


                print("Added ", self.cnt, " to stage list for below")

        # Check above
        if point.r < 0:
            above_contents = self.maze.maze[point.r-1][point.c]
            
            if above_contents == 1: # Is there obstacle
                pass
            elif above_contents == 0 and self.path_map[point.r-1][point.c] == 999: # If free, add label
                self.path_map[point.r-1][point.c] = self.cnt
                self.stage_list.append(Coord(point.r-1,point.c))


                

                #if Coord(point.r-1,point.c) == self.maze.end:
                if point.r == self.maze.end.r and point.c == self.maze.end.c:

                    print("HERE 2")
                    self.savior = False

                print("Added ", self.cnt, " to stage list for above")

        # Check Right
        if point.c < self.maze.n-1:
            right_contents = self.maze.maze[point.r][point.c+1]
            if right_contents == 1: # Is there obstacle
                pass
            elif right_contents == 0 and self.path_map[point.r][point.c+1] == 999: # If free, add label
                self.path_map[point.r][point.c+1] = self.cnt
                self.stage_list.append(Coord(point.r,point.c+1))

                #if Coord(point.r,point.c+1) == self.maze.end:
                if point.r == self.maze.end.r and point.c == self.maze.end.c:
                    print("HERE3")
                    self.savior = False

                print("Added ", self.cnt, " to stage list for right")

        # Check left
        if point.c < 0:
            left_contents = self.maze.maze[[point.r],[point.c-1]]
            if left_contents == 1: # Is there obstacle
                pass
            elif left_contents == 0 and self.path_map[point.r][point.c] == 999: # If free, add label
                self.path_map[point.r][point.c-1] = self.cnt
                self.stage_list.append(Coord(point.r,point.c-1))

                if point.r == self.maze.end.r and point.c-1 == self.maze.c:
                    print("HERE4")
                    self.savior = False
                print("Added ", self.cnt, " to stage list for left")
    
    def loop_squares(self):
        
        self.check_surround(self.maze.start)
        tmp_stage = self.stage_list
        print_coord_list(self.stage_list)

        i=0
        print("len ", len(self.stage_list))
        while self.savior:
            self.cnt += 1
            for i in self.stage_list:
                self.check_surround(i)
                #print_coord_list(i)
            #i+=1




        # for i in self.stage_list:
        #     self.cnt += 1
        #     self.check_surround(i)
        








def main():
    """Main"""
    temp = makePath()
    temp.make_map()

if __name__ == "__main__":
    main()