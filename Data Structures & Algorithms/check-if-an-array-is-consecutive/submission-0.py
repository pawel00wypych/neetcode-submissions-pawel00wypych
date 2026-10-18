class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        nums_sorted = sorted(nums)
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] - nums_sorted[i-1] != 1:
                return False
        return True
