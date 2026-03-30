class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        new_max = 0
        for n in nums:
            if n > 0:
                new_max += 1
            else:
                new_max = 0
            
            if new_max > max_ones:
                max_ones = new_max

        return max_ones