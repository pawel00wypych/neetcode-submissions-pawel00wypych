class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row_count = [0] * len(picture)
        col_count = [0] * len(picture[0])
        res = 0
        for r in range(len(picture)):
            for c in range(len(picture[r])):
                if picture[r][c] == 'B':
                    row_count[r] += 1
                    col_count[c] += 1
        
        for r in range(len(picture)):
            for c in range(len(picture[r])):
                if picture[r][c] == 'B' and row_count[r] == 1 and col_count[c] == 1:
                    res += 1

        return res
                              