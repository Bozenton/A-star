from utils import PriorityQueue
from graph_engine import WeightedGrid, Position, GridPosition
from typing import Optional, Dict
import matplotlib.pyplot as plt
from viz_engine import plot_grid

def Manhattan_distance(a: GridPosition, b: GridPosition) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

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
                priority = new_cost + Manhattan_distance(next, goal)
                priority_queue.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

def A_star_display(ax, graph: WeightedGrid, start: Position, goal: Position, time_itv=0.1):
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
            plot_grid(ax, graph, start=start, goal=goal, point_to=came_from, current=current, next=next)
            plt.waitforbuttonpress(timeout=time_itv)
            plt.draw()
            ax.cla()
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + Manhattan_distance(next, goal)
                priority_queue.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far