class MedianFinder:

    def __init__(self):
        self.small, self.big = [], []

    def addNum(self, num: int) -> None:
        if not self.big:
            heapq.heappush(self.big, num)
            return            
        
        if len(self.big) > len(self.small):
            if self.big[0] < num:
                heapq.heappush(self.small, -heapq.heappop(self.big))
                heapq.heappush(self.big, num)
            else:
                heapq.heappush(self.small, -num)
        else: # len(big) <= len(small)
            if -self.small[0] > num:
                heapq.heappush(self.big, -heapq.heappop(self.small))
                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(self.big, num)

    def findMedian(self) -> float:
        if len(self.big) > len(self.small):
            return self.big[0]
        else:
            return (self.big[0] + -self.small[0]) / 2
            
        
        