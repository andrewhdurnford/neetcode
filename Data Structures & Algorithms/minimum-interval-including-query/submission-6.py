class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        idx = defaultdict(list)
        for i, q in enumerate(queries):
            idx[q].append(i)

        res = [0] * len(queries)
        queries = sorted(list(set(queries)))

        heap = []
        i = 0

        for q in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                if intervals[i][1] >= q:
                    heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            for j in idx[q]:
                res[j] = heap[0][0] if heap else -1
    
        return res