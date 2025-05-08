import pytest
from heapqplus import MaxHeap, MaxPriorityQueue, ComplexTask

def test_heap_order():
    h = MaxHeap([3, 1, 4])
    assert h.pop() == 4
    assert h.pop() == 3
    assert h.pop() == 1

def test_key_function():
    h = MaxHeap(["a", "bbb", "cc"], key=len)
    assert h.pop() == "bbb"

def test_priority_queue():
    pq = MaxPriorityQueue()
    pq.push(1, "low")
    pq.push(5, "high")
    assert pq.pop() == (5, "high")

def test_complex_task():
    task1 = ComplexTask(name="task1", urgency=5, deadline=10)
    task2 = ComplexTask(name="task2", urgency=3, deadline=20)
    assert task2 < task1
