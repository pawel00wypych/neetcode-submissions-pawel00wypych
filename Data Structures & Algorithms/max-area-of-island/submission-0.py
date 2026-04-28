class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        max_island = 0

        def dfs(r: int,c: int) -> int:
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            count = 1
            visited.add((r,c))
            count += dfs(r-1,c)
            count += dfs(r+1,c)
            count += dfs(r,c-1)
            count += dfs(r,c+1)
            return count

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    island = 0
                    island = dfs(r,c)
                    max_island = max(max_island, island)

        return max_island