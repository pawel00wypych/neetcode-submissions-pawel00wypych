class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = dict()
        for n in nums:
            top_k[n] = top_k.get(n,0) + 1
        max_heap=[]
        for key,v in top_k.items():
            heapq.heappush(max_heap, (v*(-1), key))
        res = []
        while k > 0 and len(max_heap) > 0:

            res.append(heapq.heappop(max_heap)[1])
            k -= 1
        return res

