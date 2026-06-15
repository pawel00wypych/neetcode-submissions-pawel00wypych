class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for n in nums:
            num_dict[n] = num_dict.get(n, 0) + 1
        
        max_n = -1
        for k, v in num_dict.items():
            if max_n < k and v == 1:
                max_n = k
        return max_n