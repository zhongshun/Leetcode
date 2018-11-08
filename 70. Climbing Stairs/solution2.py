class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dp(i):
            if i not in memo:
                memo[i] = dp(i-2) + dp(i-1)
            return memo[i]
        memo = {1:1,2:2}
        return dp(n)



p = Solution()
print(p.climbStairs(5))
