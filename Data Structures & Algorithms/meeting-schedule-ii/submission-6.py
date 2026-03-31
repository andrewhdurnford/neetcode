"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        lst = []
        for i in intervals:
            lst.append([i.start, 1])
            lst.append([i.end, -1])
        
        lst = sorted(lst)
        cur = res = 0

        for i in lst:
            cur += i[1]
            res = max(res, cur)
        return res