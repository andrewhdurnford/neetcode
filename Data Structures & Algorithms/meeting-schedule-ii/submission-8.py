"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        openings = []
        for i in intervals:
            openings.append([i.start, 1])
            openings.append([i.end, -1])
        openings.sort()
        
        res = cur = 0
        for o in openings:
            cur += o[1]
            res = max(res, cur)
        
        return res