class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = nums
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i-1] + self.sums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left-1 < 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)