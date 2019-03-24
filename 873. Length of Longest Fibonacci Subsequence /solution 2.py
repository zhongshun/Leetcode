import collections
class Solution(object):
    def lenLongestFibSubseq(self, A):
        if len(A) < 3:
            return 0

        dict = {}
        self.res = 0
        def DP(j,k,A):
            if (j,k) in dict:
                return dict[(j,k)]
            dict[(j, k)] = 2
            for i in range(j):
                if DP(i,j,A) + 1 > dict[(j, k)]:
                    if A[i] + A[j] == A[k]:
                        dict[(j, k)] =dict[(i,j)] + 1
            self.res = max(self.res, dict[(j, k)])
            return dict[(j, k)]


        for i in range(len(A)-1):
            DP(i, len(A) - 1, A)
        print(dict)
        return self.res


A = [2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 21, 22, 34]
B = [ 1, 2, 3, 4, 5, 6, 7, 8]
p = Solution()
#print(p.lenLongestFibSubseq(B))
dp = collections.defaultdict(int)
print(dp)