# heapqplus

A drop-in MaxHeap and MaxPriorityQueue module for Python, with custom key support and complex object handling.
📦 Release Description (v0.1.0)


![Python package](https://img.shields.io/pypi/v/maxheapq)
![Tests](https://github.com/kunjpatel49/maxheapq/actions/workflows/python-tests.yml/badge.svg)
![License](https://img.shields.io/pypi/l/maxheapq)

🎯 What is maxheapq?
maxheapq is a Python utility package that extends the standard heapq module by providing:

✅ MaxHeap functionality using a familiar heapq-style API

🧠 Custom key function support, similar to sorted() or max()

🏗️ MaxPriorityQueue for handling (priority, item) use cases

🧱 Support for complex objects via @dataclass + @total_ordering
Built with simplicity and performance in mind, this package allows you to build max-heaps without awkward value negation hacks — all while staying Pythonic and testable.

✨ Features
MaxHeap: Push/pop max elements with optional key functions
MaxPriorityQueue: Classic (priority, value) priority queue behavior
heapify_max, heappush_max, heappop_max: Standalone utility functions
Clean, production-grade structure with full test coverage and GitHub Actions CI

🚀 Example
```python
from maxheapq import MaxHeap, MaxPriorityQueue

h = MaxHeap([1, 5, 10])
h.push(20)
print(h.pop())  # 20

pq = MaxPriorityQueue()
pq.push(2, 'background')
pq.push(10, 'critical')
print(pq.pop())  # (10, 'critical')
```

🧪 Run Tests
```bash
pytest
```
