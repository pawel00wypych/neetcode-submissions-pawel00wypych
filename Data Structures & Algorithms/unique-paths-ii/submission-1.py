class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if (obstacleGrid[0][0] == 1 or
            obstacleGrid[rows-1][cols-1] == 1 or
            (obstacleGrid[rows-1][cols-2] == 1 and 
             obstacleGrid[rows-2][cols-1] == 1)):
            return 0
        obstacleGrid[rows-1][cols-1] = 1

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if c != cols-1 or r != rows-1:
                    if obstacleGrid[r][c] == 1:
                        print(f"obstacleGrid[{r}][{c}] == 1")
                        obstacleGrid[r][c] = 0
                    elif r+1 < rows and c+1 < cols:
                        obstacleGrid[r][c] += obstacleGrid[r+1][c] + obstacleGrid[r][c+1]
                    elif r+1 < rows:
                        obstacleGrid[r][c] += obstacleGrid[r+1][c]
                    elif c+1 < cols:
                        obstacleGrid[r][c] += obstacleGrid[r][c+1]
        return obstacleGrid[0][0]