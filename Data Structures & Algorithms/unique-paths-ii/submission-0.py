class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if (obstacleGrid[rows-1][cols-1] == 1 
            or (obstacleGrid[rows-1][cols-2] == 1
                and obstacleGrid[rows-2][cols-1] == 1)):
            return 0

        prevRow = [0] * cols
        for r in range(rows-1, -1, -1):
            curRow = [0] * cols
            for c in range(cols-1, -1, -1):
                if r == rows-1 and c == cols-1:
                    curRow[c] = 1

                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                elif c+1 == cols:
                    curRow[c] += prevRow[c]
                else:
                    curRow[c] += prevRow[c] + curRow[c+1]
            prevRow = curRow

        return curRow[0]

