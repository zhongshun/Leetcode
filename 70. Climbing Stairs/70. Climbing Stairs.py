import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
#        for i in range(n):
 #           res
        memo = {}
        num2 = int(n/2)
        res = 1
        for i in range(1,num2+1):
            res += math.factorial(n-i)/math.factorial(n-i-i)/math.factorial(i)
        return int(res)


p = Solution()
print(p.climbStairs(5))
