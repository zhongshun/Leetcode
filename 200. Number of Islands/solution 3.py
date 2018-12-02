class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def Allnegiborhood(grid,y,x):
            if x >= len(grid[0]) or x < 0 or y >= len(grid) or y < 0 or grid[y][x] != '1':
                return grid
            grid[y][x] = '#'
            grid = Allnegiborhood(grid,y,x+1)
            grid = Allnegiborhood(grid,y,x-1)
            grid = Allnegiborhood(grid,y+1,x)
            grid = Allnegiborhood(grid,y-1,x)
            return grid


        if grid == []:
            return 0
        count = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == '1':
                    count += 1
                    grid = Allnegiborhood(grid,y,x)
        return count

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]


p = Solution()
print(p.numIslands(grid))
