class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix_sum = []
        row = [0] * (len(matrix[0])+1)
        self.matrix_sum.append(row)

        for ri in range(len(matrix)):
            row = [0] * (len(matrix[0])+1)
            self.matrix_sum.append(row)
            for ci in range(len(matrix[ri])):
                self.matrix_sum[ri+1][ci+1] = self.matrix_sum[ri+1][ci] + matrix[ri][ci] + self.matrix_sum[ri][ci+1] - self.matrix_sum[ri][ci]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        total = self.matrix_sum[row2+1][col2+1] - self.matrix_sum[row1][col2+1] - (self.matrix_sum[row2+1][col1] - self.matrix_sum[row1][col1])
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)