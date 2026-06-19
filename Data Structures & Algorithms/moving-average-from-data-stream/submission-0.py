class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        if len(self.queue) >= self.size:
            del self.queue[0]
        self.queue.append(val)
        res = 0.0
        for n in self.queue:
            res += n
        cur_size = len(self.queue)
        return res / cur_size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
