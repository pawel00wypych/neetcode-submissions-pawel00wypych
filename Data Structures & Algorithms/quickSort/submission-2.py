# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
from statistics import median

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs
        
    def quickSortHelper(self, pairs: List[Pair], s: int, e: int):
        if (e - s) + 1 <= 1:
            return

        #pivot_index = self.calcPivot(pairs, s, e)
        pivot_index = e
        pivot = pairs[pivot_index]
        left = s

        #temp = pairs[pivot_index]
        #pairs[pivot_index] = pairs[e]
        #pairs[e] = temp

        for i in range(s,e):
            if pairs[i].key < pivot.key:
                temp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = temp
                left += 1

        temp = pairs[e]
        pairs[e] = pairs[left]
        pairs[left] = temp

        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left+1, e)
        return

    def calcPivot(self, pairs: List[Pair], s: int, e: int) -> int:
        mid = (s+e)//2

        candidates = [
            (pairs[s].key, s), 
            (pairs[mid].key, mid),
            (pairs[e].key, e)
        ]
        candidates.sort()
        return candidates[1][1]