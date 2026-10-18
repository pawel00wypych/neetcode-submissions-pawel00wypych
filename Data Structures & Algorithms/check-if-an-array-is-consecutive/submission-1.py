class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                return False
        return True
