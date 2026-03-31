class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapq.heapify(heap)

        for num in arr:
            heapq.heappush(heap, [abs(num - x), num])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        res.sort()
        return res