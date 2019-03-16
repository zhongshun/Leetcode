class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        self.DP = {}
        def sumPath(m,n,N,i,j):
            if (i,j,N) in self.DP:
                return self.DP[i,j,N]
            elif N < 0 :
                self.DP[i,j,N] = 0
            elif i < 0 or j < 0 or i >= m or j >= n:
                self.DP[i,j,N] = 1
            else:
                self.DP[i,j,N] = sumPath(m,n,N-1,i+1,j) + sumPath(m,n,N-1,i,j+1) + sumPath(m,n,N-1,i-1,j) + sumPath(m,n,N-1,i,j-1)
            return self.DP[i,j,N]

        return sumPath(m,n,N,i,j)

m = 2
n = 2
N = 2
i = 0
j = 0


p = Solution()
print(p.findPaths(m,n,N,i,j))
