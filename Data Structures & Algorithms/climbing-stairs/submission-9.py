class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [1, 2]
        i = 2
        while i < n:
            tmp = dp[0]
            dp[0] = dp[1]
            dp[1] = tmp + dp[0]
            i += 1

        return dp[1]