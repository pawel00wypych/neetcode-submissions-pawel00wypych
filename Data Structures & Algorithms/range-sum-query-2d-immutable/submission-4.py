class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = [] * len(matrix)
        for r in range(len(matrix)):
            row = [0] * (len(matrix[r])+1)
            for c in range(len(matrix[r])):
                row[c+1] = row[c] +  matrix[r][c]
            self.sum_matrix.append(row)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2+1):
            total += self.sum_matrix[r][col2+1] - self.sum_matrix[r][col1]
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)