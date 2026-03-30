class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums):
            if i+1 < len(nums):
                j = i+1
                if nums[i] == nums[j]:
                    del nums[j]
                else:
                    i += 1
            else:
                return len(nums)

        return len(nums)