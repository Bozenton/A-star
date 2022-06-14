from typing import Protocol, Tuple, TypeVar, Optional, Iterator, List, Dict


# define type for later usage and code hinting of the IDE:
Position = TypeVar('Position')
GridPosition = Tuple[int, int]

class Graph(Protocol):
    """data structure for graph
    """
    def neighbours(self, id: Position) -> List[Position]:
        pass
    
class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.walls: List[GridPosition] = []
        
    def within_bounds(self, id: GridPosition) -> bool:
        (x, y) = id 
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id: GridPosition) -> bool:
        return id not in self.walls

    def neighbours(self, id: GridPosition) -> Iterator[GridPosition]:
        (x, y) = id 
        nbs = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
        if (x+y) % 2 == 0:
            nbs.reverse()
        results = filter(self.within_bounds, nbs)
        results = filter(self.passable, results)
        return results
    
class WeightedGrid(Grid):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        self.weights: Dict[GridPosition, float] = {}
        
    def cost(self, head: GridPosition, tail: GridPosition) -> float:
        return self.weights.get(tail, 1) # if not find, return 1


# some useful functions for visulization
# ↖↑↗←↔→↙↓↘
def draw_details(graph, id, style):
    r = " . "
    if 'number' in style and id in style['number']: r = " %-2d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = " → "
        if x2 == x1 - 1: r = " ← "
        if y2 == y1 + 1: r = " ↓ "
        if y2 == y1 - 1: r = " ↑ "
    if 'path' in style and id in style['path']:   r = " $ "
    if 'start' in style and id == style['start']: r = " A "
    if 'goal' in style and id == style['goal']:   r = " Z "
    if id in graph.walls: r = "###"
    return r

def draw_grid(graph: Grid, **details):
    print("___" * graph.width)
    for y in range(graph.height):
        for x in range(graph.width):
            print("%s" % draw_details(graph, (x,y), details), end="")
        print()
    print("~~~" * graph.width)


# some other useful functions:

def get_path_trace_back(came_from: Dict[Position, Position], 
                        start: Position, 
                        goal: Position) -> List[Position]:
    current_position: Position = goal
    path: List[Position] = []
    while current_position != start:
        path.append(current_position)
        current_position = came_from[current_position]
    path.append(start)
    path.reverse()
    return path
