class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        def dfs(i, current_list, total):
            if total == target:
                res.append(current_list.copy())
                return
            j = i
            while j < len(nums):
                if total + nums[j] > target:
                    break
                current_list.append(nums[j])
                dfs(j, current_list, total + nums[j])
                current_list.pop()
                j += 1
        dfs(0, [], 0)
        return res