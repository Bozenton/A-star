from graph_engine import WeightedGrid, draw_grid, get_path_trace_back
from Astar import A_star

grid1 = WeightedGrid(10, 10)
grid1.walls = [(1, 0), (1, 3), (1, 8), 
               (2, 5), 
               (3, 2), (3, 6), (3, 8),
               (5, 4),
               (7, 2), (7, 6), 
               (9, 0), (9, 2), (9, 8)]
start1 = (2, 2)
goal1 = (8, 8)


if __name__ == '__main__':
   came_from1, cost1 = A_star(grid1, start1, goal1)
   draw_grid(grid1, point_to=came_from1, start=start1, goal=goal1)
   print()
   draw_grid(grid1, path=get_path_trace_back(came_from1, start1, goal1))
