class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_2 = 1
        prev_1 = 2
        while n > 2:
            n -= 1
            temp = prev_1
            prev_1 = prev_1 + prev_2
            prev_2 = temp

        return prev_1