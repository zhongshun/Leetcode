class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        return 0
quality = [10,20,5]
wage = [70,50,30]
K = 2
ave = []
for i in range(len(wage)):
    ave.append(wage[i]/quality[i])
print(ave)
