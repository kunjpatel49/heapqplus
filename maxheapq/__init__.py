
from typing import Any, Callable, Iterable, Optional, List, Tuple
import heapq
from dataclasses import dataclass, field
from functools import total_ordering

class MaxHeap:
    def __init__(self, iterable: Optional[Iterable[Any]] = None, key: Optional[Callable[[Any], Any]] = None):
        self.key = key or (lambda x: x)
        self.data: List[Tuple[Any, Any]] = []

        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, item: Any):
        heapq.heappush(self.data, (-self.key(item), item))

    def pop(self) -> Any:
        return heapq.heappop(self.data)[1]

    def peek(self) -> Optional[Any]:
        return self.data[0][1] if self.data else None

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return (item for _, item in sorted(self.data, reverse=True))


class MaxPriorityQueue:
    def __init__(self):
        self.data: List[Tuple[int, Any]] = []

    def push(self, priority: int, item: Any):
        heapq.heappush(self.data, (-priority, item))

    def pop(self) -> Tuple[int, Any]:
        priority, item = heapq.heappop(self.data)
        return -priority, item

    def peek(self) -> Optional[Tuple[int, Any]]:
        if not self.data:
            return None
        priority, item = self.data[0]
        return -priority, item

    def __len__(self):
        return len(self.data)


@total_ordering
@dataclass(order=False)
class ComplexTask:
    name: str
    urgency: int = field(compare=False)
    deadline: int = field(compare=False)

    def __lt__(self, other: 'ComplexTask') -> bool:
        return (self.urgency, -self.deadline) < (other.urgency, -other.deadline)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ComplexTask):
            return False
        return (self.urgency, self.deadline) == (other.urgency, other.deadline)


# Utility functions if user wants standalone heapify-style functions
def heappush_max(heap: List[Any], item: Any, key: Optional[Callable[[Any], Any]] = None):
    k = key or (lambda x: x)
    heapq.heappush(heap, (-k(item), item))

def heappop_max(heap: List[Any]) -> Any:
    return heapq.heappop(heap)[1]

def heapify_max(iterable: Iterable[Any], key: Optional[Callable[[Any], Any]] = None) -> List[Tuple[Any, Any]]:
    k = key or (lambda x: x)
    heap = [(-k(item), item) for item in iterable]
    heapq.heapify(heap)
    return heap
