class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix)-1
  
        while L <= R:
            M = L + (R-L)//2
            if matrix[M][0] < target and matrix[M][-1] >= target:
                return self.binarySearchArray(matrix[M], target)
            elif matrix[M][0] == target:
                return True
            elif matrix[M][0] < target:
                L = M + 1
            elif matrix[M][0] > target:
                R = M - 1

        return False


    def binarySearchArray(self, arr: List[int], target: int) -> bool:
        L = 0
        R = len(arr) - 1
        print("bin search")

        while L <= R:
            M = L + (R-L)//2
            if arr[M] < target:
                L = M + 1
            elif arr[M] > target:
                R = M - 1
            elif arr[M] == target:
                return True

        return False