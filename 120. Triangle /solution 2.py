class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.DP ={ }
        def currentMin(triangle,i,j):
            if (i,j) in self.DP:
                return self.DP[(i,j)]

            if i == len(triangle) - 1:
                self.DP[(i, j)] = triangle[i][j]
                return self.DP[(i, j)]
            else:
                self.DP[(i, j)] = triangle[i][j] + min(currentMin(triangle,i+1,j), currentMin(triangle,i+1,j+1))
                return self.DP[(i, j)]

        return currentMin(triangle,0,0)
p = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(p.minimumTotal(triangle))