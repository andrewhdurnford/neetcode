"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        for i in intervals:
            rooms.append([i.start, 1])
            rooms.append([i.end, -1])
        
        rooms = sorted(rooms)
        res = 0
        cur = 0

        for r in rooms:
            cur += r[1]
            res = max(res, cur)
        
        return res
