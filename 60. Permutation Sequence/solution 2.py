class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        list = [i+1 for i in range(n)]
        res = 0
        if n ==1:
            return "1"
        for i in range(n,0,-1):
            L = math.factorial(i-1)
            ith = math.floor(k/L - 0.0001)
            res += list[ith]*10**(i-1)
            list = list[:ith] + list[ith+1:]
            k = k - ith*math.factorial(i-1)

        return str(res)
