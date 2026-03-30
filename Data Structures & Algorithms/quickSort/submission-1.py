# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        if pairs == []:
            return []

        return self.quickSort_helper(pairs, 0, len(pairs)-1)
        
    def quickSort_helper(self, pairs: List[Pair], s, e):
        if e - s + 1 <= 1:
            return pairs

        pivot = pairs[e]
        left = s
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1 

        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quickSort_helper(pairs, s, left-1)
        self.quickSort_helper(pairs, left+1, e)
        return pairs


