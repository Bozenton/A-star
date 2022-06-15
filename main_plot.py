import numpy as np
import matplotlib.pyplot as plt
import time

from graph_engine import WeightedGrid, get_path_trace_back
from Astar import A_star, A_star_display
from viz_engine import plot_grid, tellme

grid = WeightedGrid(10, 10)
# grid1.walls = [(0, 1),(3, 1),(8, 1),(5, 2),(2, 3),(6, 3),(8, 3),(4, 5),(2, 7),(6, 7),(0, 9),(2, 9),(8, 9)]
# grid1.walls = [(5, 2), (6, 3), (6, 4)]
# start1 = (1, 2)
# goal1 = (8, 8)

prepared_walls1 = [(0, 1),(3, 1),(8, 1),(5, 2),(2, 3),(6, 3),(8, 3),(4, 5),(2, 7),(6, 7),(0, 9),(2, 9),(8, 9)]

if __name__ == '__main__':
    fig, ax = plt.subplots()
    
    tellme('Key click to use prepared map,\nmouse click to select obstacles manually', ax)
    plot_grid(ax, grid)
    flag = plt.waitforbuttonpress()
    if flag == True:
        grid.walls = prepared_walls1
    elif flag == False:
        tellme("Select obstacles and press any key to finish", ax)
        obstacle = np.array(plt.ginput(-1, timeout=-1))
        obstacle = [tuple(i) for i in np.around(obstacle).astype(np.uint8)]
        obstacle = list(set(obstacle)) # remove repeated elements
        print(repr(obstacle))
        grid.walls = obstacle
    else:
        print("Something wrong happened")
        exit()
    plot_grid(ax, grid) # update image

    pts = []
    while len(pts) < 2:
        tellme("Now select the start pt and the goal pt", ax)
        pts = np.array(plt.ginput(2, timeout=-1))
        pts = np.around(pts)
        if len(pts) < 2:
            tellme('Too few points selected, starting over', ax)
            time.sleep(0.5) # wait a second
    start = tuple(pts[0])
    goal = tuple(pts[1])
    plot_grid(ax, grid, start=start, goal=goal) # update image
    
    tellme('Key click to see the process,\nmouse click to directly get result', ax)
    flag = plt.waitforbuttonpress()
    tellme('Now A star searching ...', ax)
    if flag == True:    # True if a key was pressed, 
        came_from, _ = A_star_display(ax, grid, start, goal)
    elif flag == False: # False if a mouse button was pressed
        came_from, cost = A_star(grid, start, goal)
    else:
        print("Something wrong happened")
        exit()
    plot_grid(ax, grid, point_to=came_from, path=get_path_trace_back(came_from, start, goal), start=start, goal=goal)
    tellme('Finish! Key click or mouse click to exit', ax)
    plt.waitforbuttonpress()
    # Wait for user input and return 
    # True if a key was pressed, 
    # False if a mouse button was pressed and 
    # None if no input was given within timeout seconds. 
    # Negative values deactivate timeout.
