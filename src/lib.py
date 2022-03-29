from heapq import heappush, heappop


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        heappop(self.heap)

    def empty(self):
        if not self.heap:
            return True
        else:
            return False


class Node:
    def __init__(self, parent, mat, empty_tile, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile = empty_tile
        self.level = level
        self.cost = cost
