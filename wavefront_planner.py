from importlib.resources import path
from GenerateMaze import *
"""Implementing the wavefront planner algorithm"""

class makePath:
    def __init__(self, mz):
        self.maze = mz
        # self.maze.load()
        self.cnt = 1
        self.path_map = np.full(self.maze.maze.shape, 999)
        self.stage_list = []

    def make_map(self):
        #print('Start ')
        self.maze.start.p()
        #print('End ')
        self.maze.end.p()
        
        self.path_map[self.maze.start.r][self.maze.start.c] = 0
        #self.path_map[self.maze.end.r][self.maze.end.c] = 222

        

        self.loop_squares()
        # print(self.path_map)
        # print_coord_list(self.stage_list)
        path = self.create_path()
        #self.check_surround()
        return path

    def check_surround(self, point):
        # Check bottom
        # If point is not on bottom
        # self.stage_list.clear()
        if point.r < self.maze.m-1:
            #print("Checking below")
            below_contents = self.maze.maze[point.r+1][point.c]
            
            if below_contents == 1: # Is there obstacle
                pass
            if below_contents == 0 and self.path_map[point.r+1][point.c] == 999: # If free, add label
                self.path_map[point.r+1][point.c] = self.cnt
                self.stage_list.append(Coord(point.r+1,point.c))
                # print("Added ", self.cnt, " to stage list for below")
                # print(self.path_map)
                #print("Maze: \n", self.maze.maze)

        # Check above
        if point.r > 0:
            #print("Checking above")

            above_contents = self.maze.maze[point.r-1][point.c]
            
            if above_contents == 1: # Is there obstacle
                pass
            if above_contents == 0 and self.path_map[point.r-1][point.c] == 999: # If free, add label
                self.path_map[point.r-1][point.c] = self.cnt
                self.stage_list.append(Coord(point.r-1,point.c))
                # print("Added ", self.cnt, " to stage list for above")
                # print(self.path_map)
                #print("Maze: \n", self.maze.maze)

        # Check Right
        if point.c < self.maze.n-1:
            #print("Checking right")

            right_contents = self.maze.maze[point.r][point.c+1]
            if right_contents == 1: # Is there obstacle
                pass
            if right_contents == 0 and self.path_map[point.r][point.c+1] == 999: # If free, add label
                self.path_map[point.r][point.c+1] = self.cnt
                self.stage_list.append(Coord(point.r,point.c+1))
                # print("Added ", self.cnt, " to stage list for right")
                # print(self.path_map)
                #print("Maze: \n", self.maze.maze)

        # Check left
        if point.c > 0:
            #print("Checking left")
            left_contents = self.maze.maze[[point.r],[point.c-1]]
            #print("Left contents: ", left_contents)
            #print("Path map contents", self.path_map[point.r][point.c-1])
            if left_contents == 1: # Is there obstacle
                pass
            if left_contents == 0 and self.path_map[point.r][point.c-1] == 999: # If free, add label
                self.path_map[point.r][point.c-1] = self.cnt
                self.stage_list.append(Coord(point.r,point.c-1))
                #print("Added ", self.cnt, " to stage list for left")
                #print(self.path_map)
                #print("Maze: \n", self.maze.maze)
        
        


    def are_we_there_yet(self, point):
        # print("point.r end: ", point.r, ' point.c end: ', point.c)
        # print("self.maze.end.r: ", self.maze.end.r, ' self.maze.end.c ', self.maze.end.c)
        if point.r == self.maze.end.r and point.c == self.maze.end.c:
            flag1 =  True
            #print("GOT IT BABYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYyY")
        else: 
            flag1 = False
        return flag1
    
    def loop_squares(self):
    
        self.check_surround(self.maze.start)
        #print_coord_list(self.stage_list)
        flag = False
        self.cnt += 1
        #print("Moving past start")
        while not flag:
            #print("Flag: ", flag)
            tmp_stage = np.array(self.stage_list)
            self.stage_list.clear()
            # print("tmp_stage: ", tmp_stage[1].p())
            # print_coord_list(tmp_stage)
            for i in tmp_stage:
                flag = self.are_we_there_yet(i)
                if flag == True:
                    break
                self.check_surround(i)
                # print("Flag: ", flag)
                print("TEST")
                #i.p()
            
            # print("New Stage")
            # print('count ', self.cnt)
            self.cnt += 1
            
    def create_path(self):
        y = self.maze.end.c
        x = self.maze.end.r
        current_stage = self.path_map[x,y] # Starting at end
        
        final_path = [[x,y]]
        i = 0
        size = self.path_map.shape[0] * self.path_map.shape[1]
        #print("Size: ", size)
        while i < size:
            # Check right
            if y < self.path_map.shape[1]-1:
                if self.path_map[x,y+1] == 999:
                    pass
                elif self.path_map[x,y+1] < current_stage:
                    #print("right clear")
                    final_path.append([x, y+1])
                    current_stage -= 1
                    y += 1

            # Check left
            if y > 0:
                if self.path_map[x,y-1] == 999:
                    pass
                elif self.path_map[x,y-1] < current_stage:
                    #print("left clear")
                    final_path.append([x, y-1])
                    current_stage -= 1
                    y -= 1 

            # Check above
            if x > 0:
                if self.path_map[x-1,y] == 999:
                    pass
                elif self.path_map[x-1,y] < current_stage:
                    #print("above clear")
                    final_path.append([x-1, y])
                    current_stage -= 1
                    x -= 1

            # Check below
            if x < self.path_map.shape[0]-1:
                if self.path_map[x+1,y] == 999:
                    pass
                elif self.path_map[x+1,y] < current_stage:
                    #print("below clear")
                    final_path.append([x+1, y])
                    current_stage -= 1
                    x += 1       
            i+= 1
        final_path.reverse()
        #print("Final Path ", final_path)
        return final_path

        

def main():
    """Main"""
    temp = makePath()
    done = temp.make_map()
    print(done)
    

if __name__ == "__main__":
    main()