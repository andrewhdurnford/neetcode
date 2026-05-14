"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ints = [[i.start, i.end] for i in intervals]
        ints.sort()

        for i in range(1 , len(ints)):
            prev, cur = ints[i - 1], ints[i]
            if prev[1] > cur[0]:
                return False
        return True