class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        z = 0
        prefix = {}
        for n in nums:
            if n != 0:
                total *= n
            else:
                z += 1
        
        output = [0] * len(nums)
        if z > 1:
            return output

        for i in range(len(nums)):
            if nums[i] != 0 and z>0:
                output[i] = 0
            elif nums[i] != 0:
                output[i] = total//nums[i]
            else:
                output[i] = total
        return output