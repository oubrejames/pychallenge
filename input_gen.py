from turtle import st
import numpy as np
import random

test_maze1 = np.array([[1,0,0,0,1,1],[1,0,1,1,1,0],[1,1,1,0,1,0],[0,1,1,0,1,0],[0,0,0,0,1,1],[0,0,0,0,0,1]])
#print("one: \n", test_maze1)
start1 = [0,0]
end1 = [5,5]

test_maze2 = np.array([[0,0,1,0,0,0],[0,0,1,0,0,0],[0,0,1,1,1,0],[1,1,1,1,1,0],[0,0,0,0,1,1],[1,1,1,1,1,0]])
#print("two: \n",test_maze2)
start2 = [0,2]
end2 = [5,0]

test_maze3 = np.array([[0,0,1,0,0,0],[0,0,1,0,0,0],[0,0,1,1,1,0],[1,1,1,1,1,0],[0,0,1,0,1,1],[1,1,1,1,1,0]])
#print("three: \n",test_maze3)
start3 = [0,2]
end3 = [5,0]

test_maze4 = np.array([[0,0,0,0,1,1],[1,0,1,1,1,0],[0,0,0,0,1,1],[0,1,1,0,1,0],[1,0,0,0,1,1],[1,1,1,0,1,0]])
#print("four: \n",test_maze4)
start4 = [0,5]
end4 = [5,4]

test_maze5 = np.array([[1,1,1,1,1,0],[0,0,1,0,0,0],[0,0,1,0,1,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[0,0,1,1,1,0]])
#print("five: \n",test_maze5)
start5 = [0,4]
end5 = [5,2]

test_maze6 = np.array([[0,0,1,0,0,0],[0,0,1,1,0,0],[1,1,0,1,1,0],[0,0,1,1,0,0],[1,1,1,1,1,0],[0,0,1,0,1,1]])
#print("six: \n",test_maze6)
start6 = [0,2]
end6 = [5,5]

test_maze7 = np.array([[1,0,0,0,1,1],[1,0,1,1,1,0],[1,1,1,0,1,0],[0,1,1,0,1,0],[0,0,0,0,1,1],[0,0,0,0,0,1]])
#print("one: \n", test_maze1)
start7 = [0,5]
end7 = [5,5]

test_maze8 = np.array([[1,1,1,1,1,0],[0,0,1,0,0,0],[0,0,1,0,1,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[0,0,1,1,1,0]])
#print("five: \n",test_maze5)
start8 = [2,2]
end8 = [5,2]

mazes = [test_maze1,test_maze2,test_maze3,test_maze4,test_maze5,test_maze6,test_maze7,test_maze8]
starts = [start1, start2, start3, start4, start5, start6, start7, start8]
ends = [end1,end2, end3, end4, end5, end6, end7, end8]

def give_rand_maze():
    """Provide a random maze from the selction of predefined mazes"""
    num = random.randint(0,7)
    return mazes[num], starts[num], ends[num]

tmaze, tstart, tend = give_rand_maze()
print(tmaze)
print(tstart)
print(tend)