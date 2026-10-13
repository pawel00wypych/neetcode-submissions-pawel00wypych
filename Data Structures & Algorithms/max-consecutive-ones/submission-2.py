class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        n_max = 0

        for i in nums:
            if i != 1:
                n = 0
            else:
                n += 1
                if n > n_max:
                    n_max = n

        return n_max