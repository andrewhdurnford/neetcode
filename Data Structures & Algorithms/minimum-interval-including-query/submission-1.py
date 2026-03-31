class Solution:
    def minInterval(self, intervals, queries):
        import heapq
        # Sort intervals based on their starting point
        intervals.sort()
        # Sort queries and keep track of their original indices
        sorted_queries = sorted([(q, idx) for idx, q in enumerate(queries)])
        # Initialize a min-heap
        min_heap = []
        res = [-1] * len(queries)
        i = 0  # Index for intervals
        n = len(intervals)
        for q, idx in sorted_queries:
            # Add all intervals starting before or at the query point
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                # Only consider intervals that can cover the query point
                if r >= q:
                    heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            # Remove intervals that end before the query point
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            # The top of the heap is the smallest interval covering the query
            if min_heap:
                res[idx] = min_heap[0][0]
            else:
                res[idx] = -1
        return res
