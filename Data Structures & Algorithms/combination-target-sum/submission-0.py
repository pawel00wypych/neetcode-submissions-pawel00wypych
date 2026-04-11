class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def dfs(i, cur_sum):
            if cur_sum == target:
                res.append(sub.copy())
                return
            if i >= len(nums):
                return
            if cur_sum > target:
                return
            sub.append(nums[i])
            dfs(i, cur_sum+nums[i])
            sub.pop()
            dfs(i+1, cur_sum)
            
        dfs(0,0)
        return res