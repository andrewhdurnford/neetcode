"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        ints = []
        for i in intervals:
            ints.append([i.start, i.end])
        ints.sort()

        res = 1
        heap = [ints[0][1]]

        for i in range(1, len(ints)):
            while heap and heap[0] <= ints[i][0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, ints[i][1])
            res = max(res, len(heap))
        
        return res