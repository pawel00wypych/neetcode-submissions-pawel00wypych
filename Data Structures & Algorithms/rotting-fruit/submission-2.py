class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        ROW, COL = len(grid), len(grid[0])
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
        layer = deque()
        fresh_cells = set()
        visit = set()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    layer.append((i,j))
                elif grid[i][j] == 1:
                    fresh_cells.add((i,j))
        
        if len(fresh_cells) == 0:
            return 0
        if len(layer) == 0:
            return -1
            
        while layer:
            for i in range(len(layer)):
                r, c = layer.popleft()
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if (min(row, col) < 0 or
                            row == ROW or
                            col == COL or
                            grid[row][col] == 0 or
                            (row, col) in visit):
                        continue
                    elif grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh_cells.remove((row,col))
                        layer.append((row,col))
                        visit.add((row,col))
                    elif grid[row][col] == 2:
                        layer.append((row,col))
                        visit.add((row,col)) 
            minutes += 1
            if len(fresh_cells) == 0:
                return minutes
        return -1 if len(fresh_cells) > 0 else minutes