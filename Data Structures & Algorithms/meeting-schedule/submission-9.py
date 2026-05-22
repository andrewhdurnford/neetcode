"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ints = []
        for i in intervals:
            ints.append([i.start, i.end])
        ints.sort()

        for i in range(1, len(ints)):
            if ints[i - 1][1] > ints[i][0]:
                return False

        return True