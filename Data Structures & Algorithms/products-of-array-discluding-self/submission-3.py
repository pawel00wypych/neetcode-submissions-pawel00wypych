class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        output[0] = nums[0]

        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i]

        postfix = 1
        for i in range(len(nums)):
            if i == len(nums)-1:
                output[len(nums) - i -1] = postfix
            else:
                output[len(nums) - i -1] = postfix * output[len(nums) - i -2]
            postfix *= nums[len(nums)-i-1]

        return output