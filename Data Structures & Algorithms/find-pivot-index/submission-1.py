class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        left_to_right = {}
        for i in range(len(nums)-1, -1, -1):
            right_sum += nums[i]
            left_to_right[i] = right_sum

        for i in range(0, len(nums)):
            left_sum += nums[i]
            if i in left_to_right and left_to_right[i] == left_sum:
                return i

        return -1