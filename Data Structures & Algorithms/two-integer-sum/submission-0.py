class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        i = 0
        j = 1
        while i < len(nums)-1:
            if nums[i] + nums[j] == target:
                res.append(i)
                res.append(j)
            j += 1
            if j > len(nums)-1:
                i += 1
                j = i + 1

        return res