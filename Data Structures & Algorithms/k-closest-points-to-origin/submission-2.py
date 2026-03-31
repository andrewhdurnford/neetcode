class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []

        for p in points:
            d = -(p[0] ** 2 + p[1] ** 2)
            heapq.heappush(maxHeap, [d, p[0], p[1]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = [] 
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        
        return res