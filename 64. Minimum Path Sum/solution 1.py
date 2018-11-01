class Solution(object):
    def minPathSum(self, grid):

        Input = grid
        dp = []
        for i in range(len(Input)):
            dp = dp + [len(Input[0])*[0]]

        dp[0][0] = Input[0][0]

        for x in range(1,len(Input[0])):
            dp[0][x] = dp[0][x-1] + Input[0][x]


        for y in range(1,len(Input)):
            dp[y][0] = dp[y-1][0] + Input[y][0]


        for y in range(1,len(Input)):
            for x in range(1,len(Input[0])):
                dp[y][x] = min(dp[y][x-1] + Input[y][x], dp[y-1][x] + Input[y][x])
        return dp[-1][-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
p = Solution()
print(p.minPathSum(grid))
