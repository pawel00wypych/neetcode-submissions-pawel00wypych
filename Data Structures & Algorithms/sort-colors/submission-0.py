class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {'0': 0, '1': 0, '2': 0}
        for n in nums:
                colors[str(n)] += 1

        i = 0
        while i < len(nums):
            for k, v in colors.items():
                while v > 0:
                    nums[i] = k
                    v -= 1
                    i += 1
                
