class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROW = len(grid)
        COL = len(grid[0])
        count = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] == '0' or (r, c) in visited:
                return

            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r, c)
                    count += 1

        return count