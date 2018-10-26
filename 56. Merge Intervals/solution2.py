class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


s1 = Interval(1,3)
s2 = Interval(2,6)
s3 = Interval(8,10)
s4 = Interval(15,18)
s5 = Interval(4,7)
intervals = [s1,s2,s3,s4]
intervals.sort(key=lambda i:i.start)
for i in range(4):
    print(intervals[i].start,intervals[i].end)
