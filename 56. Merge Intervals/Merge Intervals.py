
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ########sort
        for i in range(len(intervals)):
            dic_start += [intervals[i].start]

        List_Sort = []
        for i in range(len(intervals)):
            min_i = dic_start.index(min(dic_start))
            List_Sort += [intervals[min_i]]
            dic_start = dic_start[0:min_i] + dic_start[min_i+1:]
            intervals = intervals[0:min_i] + intervals[min_i+1:]

        ###########################
        while True:
            if i >= len(List_Sort)-1:
                break

            if List_Sort[i].end >=  List_Sort[i+1].start:
                print(List_Sort[i].start,List_Sort[i].end,List_Sort[i+1].start,List_Sort[i+1].end )
                List_Sort[i].end =  max(List_Sort[i].end, List_Sort[i+1].end)
                List_Sort = List_Sort[0:i+1] + List_Sort[i+2:]
            else:
                i = i + 1

        return List_Sort





s1 = Interval(1,3)
s2 = Interval(2,6)
s3 = Interval(8,10)
s4 = Interval(15,18)
s5 = Interval(4,7)
intervals = [s1,s2,s3,s4]
dic_start = []
for i in range(len(intervals)):
    dic_start += [intervals[i].start]
print(dic_start)
List_Sort = []
for i in range(len(intervals)):
    min_i = dic_start.index(min(dic_start))
    List_Sort += [intervals[min_i]]
    dic_start = dic_start[0:min_i] + dic_start[min_i+1:]
    intervals = intervals[0:min_i] + intervals[min_i+1:]
print(List_Sort)
for s in List_Sort:
    print(s.start,s.end)

i = 0
while True:
    if i >= len(List_Sort)-1:
        break

    if List_Sort[i].end >=  List_Sort[i+1].start:
        print(List_Sort[i].start,List_Sort[i].end,List_Sort[i+1].start,List_Sort[i+1].end )
        List_Sort[i].end =  max(List_Sort[i].end, List_Sort[i+1].end)
        List_Sort = List_Sort[0:i+1] + List_Sort[i+2:]
    else:
        i = i + 1
print("###############################")
for s in List_Sort:
    print(s.start,s.end)
