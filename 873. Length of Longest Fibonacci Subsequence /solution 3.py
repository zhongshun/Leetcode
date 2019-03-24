import collections
class Solution:
    def lenLongestFibSubseq(self, A):
        dp = collections.defaultdict(int)
        s = set(A)
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
        print(dp.values())
        return max(dp.values() or [0])

A = [2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 21, 22, 34]
B = [ 1, 2, 3, 4, 5, 6, 7, 8]
p = Solution()
print(p.lenLongestFibSubseq(B))