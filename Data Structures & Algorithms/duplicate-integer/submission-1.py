class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_d = {}
        for n in nums:
            if n in num_d:
                return True
            else:
                num_d[n] = 1
        return False