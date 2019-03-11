from heapq import *
class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

obj = MedianFinder()
obj.addNum(1)
obj.addNum(5)
obj.addNum(7)
obj.addNum(8)
obj.addNum(0)
obj.addNum(4)
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)
