from importlib.resources import path
from input_gen import *

"""Implementing the wavefront planner algorithm"""

def find_path():
    path = []
    current_pos = [start[0], start[1]]
    path.append(current_pos[:])

def check_surroundings(mze, current_point, pathmap, cnt):

    #Check below
    # below_sq = mze[[current_point[0]-1] [current_point[1]]]
    if current_point[1] != mze.shape[1]+1: 
        # If the current point is not at the bottom
        print("x ", current_point[0])
        print('y ', current_point[1]+1)
        below_sq = mze[[current_point[0]] [current_point[1]+1]]

        if below_sq == 0: 
            # If below square is a 0 (obsticle) mark -1
            pathmap[[below_sq[0]][below_sq[1]]] = -1
        elif below_sq == 1:
            # Add clear label (number)
            pathmap[[below_sq[0]][below_sq[1]]] = cnt


    #Check Above
    
    if current_point[1] != 0:
        # If the current point is on the top aka above square out of bounds
        above_sq = mze[[current_point[0]] [current_point[1]+1]]
        if above_sq == 0: 
            # If below square is a 0 (obsticle) mark -1
            pathmap[[above_sq[0]][above_sq[1]]] = -1
        elif above_sq == 1:
            # Add clear label (number)
            pathmap[[above_sq[0]][above_sq[1]]] = cnt


    #Check left
    left_sq = mze[[current_point[0]] [current_point[1]-1]]
    if current_point[0] == 0:
        # If the current point is on the left boundry aka left square out of bounds
        pass
    elif left_sq == 0: 
        # If below square is a 0 (obsticle) mark -1
        pathmap[[left_sq[0]][left_sq[1]]] = -1
    elif left_sq == 1:
        # Add clear label (number)
        pathmap[[left_sq[0]][left_sq[1]]] = cnt


    #Check Right
    right_sq = mze[[current_point[0]] [current_point[1]+1]]
    if current_point[0] == mze.shape[0]:
        # If the current point is on the right boundry aka right square out of bounds
        pass
    elif right_sq == 0: 
        # If below square is a 0 (obsticle) mark -1
        pathmap[[right_sq[0]][right_sq[1]]] = -1
    elif right_sq == 1:
        # Add clear label (number)
        pathmap[[right_sq[0]][right_sq[1]]] = cnt

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