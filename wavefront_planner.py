from importlib.resources import path
from input_gen import *

"""Implementing the wavefront planner algorithm"""

def find_path():
    path = []
    current_pos = [start[0], start[1]]
    path.append(current_pos[:])

def check_surroundings(mze, current_point, pathmap, cnt):

    # Check Below
    


def make_map(mze, start, end):
    print('Start point: ', start)
    print('End point ', end)
    #print(mze[start[0]][start[1]])

    path_map = np.empty(mze.shape)
    path_map[start[0]][start[1]] = 0
    cnt = 0
    check_surroundings(mze, start, path_map, cnt)




def main():
    """Main"""
    maze, start_point, end_point = give_rand_maze()
    make_map(maze, start_point, end_point)

if __name__ == "__main__":
    main()