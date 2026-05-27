class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        idx = defaultdict(list)
        for i, q in enumerate(queries):
            idx[q].append(i)

        queries.sort()

        # init res array with -1
        res = [-1] * len(queries)

        # min heap indexed on interval length
        heap = []
        i = 0

        for q in queries:
            # pop intervals in heap that are too small
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # skip intervals that are too small
            while i < len(intervals) and intervals[i][1] < q:
                i += 1
            
            # add intervals that q is in
            while i < len(intervals) and intervals[i][0] <= q:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (length, intervals[i][1]))
                i += 1
            
            # heap now contains all intervals q is in, sorted by length
            if heap:
                minlength = heap[0][0]
                for j in idx[q]:
                    res[j] = minlength
        
        return res
            