class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)-1
        mid = L + (R-L)//2

        while L <= R:
            if target < nums[mid]:
                R = mid - 1
                mid = L + (R-L)//2
            elif target > nums[mid]:
                L = mid + 1
                mid = L + (R-L)//2
            elif target == nums[mid]:
                return mid
        
        return -1