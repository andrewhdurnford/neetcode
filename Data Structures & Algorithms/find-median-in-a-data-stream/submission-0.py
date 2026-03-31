class MedianFinder:

    def __init__(self):
        self.sh = []
        self.bh = []

    def addNum(self, num: int) -> None:
        if self.bh and num > self.bh[0]:
            heapq.heappush(self.bh, num)
        else:
            heapq.heappush(self.sh, -num)
        
        if len(self.sh) < (len(self.bh) - 1):
            heapq.heappush(self.sh, -heapq.heappop(self.bh))
        elif len(self.bh) < (len(self.sh) - 1):
            heapq.heappush(self.bh, -heapq.heappop(self.sh))

    def findMedian(self) -> float:
        if len(self.sh) == len(self.bh):
            return ((self.bh[0] - self.sh[0]) / 2)
        elif len(self.sh) < len(self.bh):
            return self.bh[0]
        else:
            return -self.sh[0]