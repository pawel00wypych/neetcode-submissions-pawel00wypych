class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        prev_row = [0] * cols
        cur_row = [0] * cols
        for r in range(rows-1, -1, -1):
            cur_row = [0] * cols
            cur_row[cols-1] = 1
            for c in range(cols-2, -1, -1):
                cur_row[c] = cur_row[c+1] + prev_row[c]
            prev_row = cur_row

        return cur_row[0]