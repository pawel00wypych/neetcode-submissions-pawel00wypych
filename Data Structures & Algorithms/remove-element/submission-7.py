class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, (len(nums)-1)
        k = 0
        while left <= right:
            if nums[left] == val:
                while nums[right] == val and left <= right:
                    right -= 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    k += 1
            else:
                k += 1
            left += 1
        return k