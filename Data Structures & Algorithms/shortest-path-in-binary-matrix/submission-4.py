class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        length = 1
        ROW, COL = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROW-1][COL-1]:
            return -1
        layer = deque([(0,0)])
        grid[0][0] = 1

        directions = [
                    (-1, 0), (1, 0), (0, -1), (0, 1),   # 4 directions
                    (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonals
        ]

        while layer:
            for i in range(len(layer)):
                r, c = layer.popleft()
                if r == ROW-1 and c == COL-1:
                    return length

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (min(col, row) < 0 or
                        col == COL or
                        row == ROW or
                        grid[row][col] == 1):
                        continue
                    grid[row][col] = 1
                    layer.append((row,col))

            length += 1
        return -1