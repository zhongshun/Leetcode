import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """




n = 8
k = 13801
list = [i+1 for i in range(n)]
res = []
for i in range(n,0,-1):
    L = math.factorial(i-1)
    ith = math.floor(k/L - 0.0001)

    res.append(list[ith])
    list.remove(list[ith])
    k = k - ith*math.factorial(i-1)

print(res)
r = 0
for i in range(len(res)):
    r += res[i]*10**(len(res)-1-i)
print(str(r))
