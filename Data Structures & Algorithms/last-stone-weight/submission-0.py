class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-n for n in stones]  
        heapq.heapify(q)
        while len(q) > 1:
            x, y = heapq.heappop(q), heapq.heappop(q)
            if x - y != 0:
                heapq.heappush(q, -abs(x - y))
        
        if len(q) == 0:
            return 0
        
        return -heapq.heappop(q)
