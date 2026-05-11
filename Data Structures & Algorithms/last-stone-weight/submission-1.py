class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(-s)
        heapq.heapify(heap)

        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            if not a == b:
                heapq.heappush(heap, -abs(a - b))
        
        return -heap[0] if heap else 0