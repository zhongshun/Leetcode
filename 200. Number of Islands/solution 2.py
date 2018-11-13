class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def Allnegiborhood(grid,y,x,memo):
            if x+1 < len(grid[0]):
                if grid[y][x+1] == '1' and memo[y][x+1] == 0:
                    memo[y][x+1] = 1
                    memo = Allnegiborhood(grid,y,x+1,memo)

            if x-1 >= 0:
                if grid[y][x-1] == '1' and memo[y][x-1] == 0:
                    memo[y][x-1] = 1
                    memo = Allnegiborhood(grid,y,x-1,memo)

            if y+1 < len(grid):
                if grid[y+1][x] == '1' and memo[y+1][x] == 0:
                    memo[y+1][x] = 1
                    memo = Allnegiborhood(grid,y+1,x,memo)

            if y-1 >= 0:
                if grid[y-1][x] == '1' and memo[y-1][x] == 0:
                    memo[y-1][x] = 1
                    memo = Allnegiborhood(grid,y-1,x,memo)
            return memo

        memo = []
        for x in range(len(grid)):
            new = []
            for y in range(len(grid[0])):
                    new.append(0)
            memo.append(new)


        if grid == []:
            return 0
        count = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == '1' and memo[y][x] == 0:
                    count += 1
                    Allnegiborhood(grid,y,x,memo)
        return count

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]


p = Solution()
print(p.numIslands(grid))
