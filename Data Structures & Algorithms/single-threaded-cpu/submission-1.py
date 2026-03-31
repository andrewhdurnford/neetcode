class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        available = []
        res = []
        time = 0

        for i, t in enumerate(tasks):
            enqueueTime, processTime = t
            heapq.heappush(heap, (enqueueTime, processTime, i))
        
        while heap or available:
            if heap:
                time = max(time, heap[0][0])

            while heap and heap[0][0] <= time:
                enqueueTime, processTime, i = heapq.heappop(heap)
                heapq.heappush(available, (processTime, i))

            processTime, i = heapq.heappop(available)
            time += processTime
            res.append(i)
        
        return res