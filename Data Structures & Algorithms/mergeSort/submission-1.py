# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        m = int(len(pairs)/2)
        e = len(pairs)
        l = self.mergeSort(pairs[:m])
        r = self.mergeSort(pairs[m:e])

        merged = self.merge(l, r)
        return merged


    def merge(self, p1, p2):
        i = 0
        j = 0
        result = []
        while i < len(p1) and j < len(p2):
            if p1[i].key <= p2[j].key:
                result.append(p1[i])
                i += 1
            else:
                result.append(p2[j])
                j += 1

        while i < len(p1):
            result.append(p1[i])
            i += 1
            
        while j < len(p2):
            result.append(p2[j])
            j += 1

        return result
