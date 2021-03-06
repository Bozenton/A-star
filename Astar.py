from graph_engine import WeightedGrid, Position, GridPosition, get_path_trace_back
from typing import Optional, Dict
import matplotlib.pyplot as plt
import numpy as np
import os
from time import gmtime, strftime

from viz_engine import plot_grid
from utils import PriorityQueue


def Manhattan_distance(a: GridPosition, b: GridPosition) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def Euclidean_distance(a: GridPosition, b: GridPosition) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def A_star(graph: WeightedGrid, start: Position, goal: Position):
    priority_queue = PriorityQueue()
    priority_queue.put(start, 0)
    came_from: Dict[Position, Optional[Position]] = {}
    cost_so_far: Dict[Position, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not priority_queue.is_empty():
        current: Position = priority_queue.get()
        
        if current == goal:
            break
        
        for next in graph.neighbours(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + Euclidean_distance(next, goal)
                priority_queue.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

def A_star_display(ax, graph: WeightedGrid, start: Position, goal: Position, time_itv=0.1, save=False):
    priority_queue = PriorityQueue()
    priority_queue.put(start, 0)
    came_from: Dict[Position, Optional[Position]] = {}
    cost_so_far: Dict[Position, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    if save:
        folder_name = strftime("%Y-%m-%d-%H-%M-Astar", gmtime())
        if not os.path.exists(folder_name):
            os.system('mkdir '+folder_name)
    
    cnt = 0
    while not priority_queue.is_empty():
        current: Position = priority_queue.get()
        if current == goal:
            break
                
        for next in graph.neighbours(current):
            ax.cla()
            plot_grid(ax, graph, start=start, goal=goal, 
                      point_to=came_from, 
                      current=current, next=next, 
                      path=get_path_trace_back(came_from, start, current))
            plt.waitforbuttonpress(timeout=time_itv)
            if save:
                plt.savefig(os.path.join(folder_name, f'step%03d.png'%cnt), bbox_inches='tight', transparent=True, dpi=100)
            plt.draw()
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + Euclidean_distance(next, goal)
                priority_queue.put(next, priority)
                came_from[next] = current
            cnt = cnt + 1
    
    return came_from, cost_so_far