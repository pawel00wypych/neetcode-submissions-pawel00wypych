class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        length = 0
        visit = set()
        layer = deque()
        layer.append((0,0))
        ROW, COL = len(grid), len(grid[0])

        while layer:
            for i in range(len(layer)):
                r, c = layer.popleft()
                if r == ROW-1 and c == COL-1:
                    return length

                directions = [(-1,0), (1,0), (0,-1), (0,1)] #up, down, left, right
                for dr, dc in directions:
                    if (min(r+dr,c+dc) < 0 or 
                        (r+dr,c+dc) in visit or 
                        r+dr == ROW or 
                        c+dc == COL or 
                        grid[r+dr][c+dc] == 1):
                        continue
                        
                    layer.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
            length += 1
        return -1