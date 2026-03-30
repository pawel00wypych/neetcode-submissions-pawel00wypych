class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        i = 3
        prev_2 = 1
        prev_1 = 2
        new_sol = prev_1 + prev_2 
        while i <= n:
            i += 1
            new_sol = prev_1 + prev_2 
            prev_2 = prev_1
            prev_1 = new_sol

        return new_sol