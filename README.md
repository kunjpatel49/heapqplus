# maxheapq

A Python module that adds MaxHeap and MaxPriorityQueue functionality with full support for custom key functions and complex objects.

![Python package](https://img.shields.io/pypi/v/maxheapq)
![Tests](https://github.com/kunjpatel49/maxheapq/actions/workflows/python-tests.yml/badge.svg)

## Features
- MaxHeap using standard heapq under the hood
- Custom comparator (key function) support
- PriorityQueue interface for (priority, item) use cases
- Support for dataclass-based complex sorting

## Installation
```bash
pip install maxheapq
```

## Example Usage
```python
from maxheapq import MaxHeap, MaxPriorityQueue, ComplexTask

h = MaxHeap([1, 10, 5])
h.push(20)
print(h.pop())  # 20

pq = MaxPriorityQueue()
pq.push(5, 'low')
pq.push(10, 'urgent')
print(pq.pop())  # (10, 'urgent')
```
