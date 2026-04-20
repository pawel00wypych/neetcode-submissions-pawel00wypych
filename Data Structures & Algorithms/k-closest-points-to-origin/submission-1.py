class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            dist = self.euclideanDistance(point)
            heapq.heappush(max_heap, (-1 * dist, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        res = []
        for tup in max_heap:
            res.append(tup[1])
        return res

    def euclideanDistance(self, point: List[int])-> int:
        return point[0]**2 + point[1]**2