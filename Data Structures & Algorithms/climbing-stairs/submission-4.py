class Solution:
    def __init__(self):
        self.cache = {}
        self.cache[0] = 0
        self.cache[1] = 1
        self.cache[2] = 2

    def climbStairs(self, n: int) -> int:

        if n in self.cache:
            return self.cache[n] 
        else:
            self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.cache[n] 