class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    intervals.sort(key=lambda i:i.start)
    Meged = []
    for s in intervals:
        if Meged and Meged[-1].end >= s.start:
            Meged[-1].end = max(s.end,Meged[-1].end)
        else:
            Meged += [s]
    return Meged

s1 = Interval(1,3)
s2 = Interval(2,6)
s3 = Interval(8,10)
s4 = Interval(15,18)
s5 = Interval(4,7)
intervals = [s1,s2,s3,s4]

mege = merge(intervals)
for i in range
