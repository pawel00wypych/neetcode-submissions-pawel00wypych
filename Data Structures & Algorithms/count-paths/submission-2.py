class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur_row = [1] * n
        for r in range(m-1):
            for i in range(n-2, -1, -1):
                cur_row[i] = cur_row[i] + cur_row[i+1]


        return cur_row[0]