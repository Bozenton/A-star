import collections 
import heapq
from typing import List, Tuple, TypeVar

T = TypeVar('T')

class Queue:
    def __init__(self) -> None:
        self.deque = collections.deque()
    
    def is_empty(self) -> bool:
        return not self.deque
    
    def put(self, x):
        self.deque.append(x)
        
    def get(self):
        return self.deque.popleft() # first in, first out

class PriorityQueue:
    def __init__(self) -> None:
        self.elements: List[Tuple[float, T]] = []
        
    def is_empty(self) -> bool:
        return not self.elements
    
    def put(self, item, priority:float):
        """put the item into the priority queue with priority value
            
        Args:
            item (_type_): item to put in the priority queue
            priority (float): priority value
        """
        heapq.heappush(self.elements, (priority, item))
        
    def get(self):
        """pop the item with highest priority in the queue

        Returns:
            _type_: item with highest priority
        """
        return heapq.heappop(self.elements)[1]
    
    def items(self):
        return list(item for _, item in self.elements)
    
    
