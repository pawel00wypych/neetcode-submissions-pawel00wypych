class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        max_n = 0
        for n in nums:
            if n == 1:
                max_n += 1
            else:
                if max_n > max_num:
                    max_num = max_n
                max_n = 0
                    
        return max_n if max_n > max_num else max_num