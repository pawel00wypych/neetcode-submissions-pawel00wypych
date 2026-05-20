class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        cur_row = [1] * cols
        for r in range(rows-1):
            for i in range(cols-2, -1, -1):
                cur_row[i] = cur_row[i] + cur_row[i+1]


        return cur_row[0]