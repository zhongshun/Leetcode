import collections
class Solution(object):
    def lenLongestFibSubseq(self, A):
        dp = {}
        s = set(A)
        res = 0
        for i in range(len(A)):
            for j in range(i):
                if A[i] - A[j] < A[j] and A[i] - A[j] in s:
                    if (A[i] - A[j], A[j]) not in dp:
                        dp[(A[i] - A[j], A[j])] = 2
                    dp[A[j], A[i]] = dp[(A[i] - A[j], A[j])] + 1
                    res = max(res,dp[A[j], A[i]])
        if res < 3:
            return 0
        print(dp)
        return res

A = [2,4,5,6,7,8,11, 13,14,15, 21,22, 34]
B = [1,2,3,4,5,6,7,8]
p = Solution()
print(p.lenLongestFibSubseq(B))
