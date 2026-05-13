class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        if not self.min or num > self.min[0]:
            heapq.heappush(self.min, num)
        else:
            heapq.heappush(self.max, -num)

        # min more than one larger than max
        if len(self.min) > len(self.max) + 1:
            heapq.heappush(self.max, -heapq.heappop(self.min))
        # max larger than min
        elif len(self.max) > len(self.min):
            heapq.heappush(self.min, -heapq.heappop(self.max))


    def findMedian(self) -> float:
        if not self.min: return None

        if len(self.min) == len(self.max):
            return (self.min[0] - self.max[0]) / 2
        else:
            return self.min[0]
        