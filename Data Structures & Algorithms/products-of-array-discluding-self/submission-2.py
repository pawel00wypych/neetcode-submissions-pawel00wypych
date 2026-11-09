class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefix = [1] * (len(nums)+1)
        suffix = [1] * (len(nums)+1)

        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]
            suffix[len(nums)-1-i] = suffix[len(nums)-i] * nums[len(nums)-i-1]
        
        for i in range(len(nums)):
            output[i] = suffix[i+1] * prefix[i]

        return output
