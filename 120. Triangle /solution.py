class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        def currentMin(triangle,i,j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            else:
                return triangle[i][j] + min(currentMin(triangle,i+1,j), currentMin(triangle,i+1,j+1))

        return currentMin(triangle,0,0)

p = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(p.minimumTotal(triangle))