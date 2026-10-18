import heapq 

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.min_heap, val)

    def pop(self) -> None:
        val = self.stack.pop()
        for i in range(len(self.min_heap)):
            if self.min_heap[i] == val:
                self.min_heap[i] = self.min_heap[-1]
                self.min_heap.pop()
                heapq.heapify(self.min_heap)
                return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_heap[0]
