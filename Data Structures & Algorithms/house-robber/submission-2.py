class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        i = 0
        def dfs(i):
            if i > len(nums)-1:
                return 0
            if i not in dp:
                dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            
            return dp[i]

        return max(nums[i] + dfs(i+2), dfs(i+1))