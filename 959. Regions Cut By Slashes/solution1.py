Input = [
  " /",
  "/ "
]

def RegionCount(BigGraph,x,y):
    BigGraph[x][y] = 9
    if x < len(BigGraph) - 1:
        if BigGraph[x+1][y] == 0:
            BigGraph = RegionCount(BigGraph,x+1,y)
    if x > 0:
        if BigGraph[x-1][y] == 0:
            BigGraph = RegionCount(BigGraph,x-1,y)
    if y < len(BigGraph) - 1:
        if BigGraph[x][y+1] == 0:
            BigGraph = RegionCount(BigGraph,x,y+1)
    if y > 0:
        if BigGraph[x][y-1] == 0:
            BigGraph = RegionCount(BigGraph,x,y-1)
    return BigGraph


grid = Input


n = len(grid)
res = 0
BigGraph = []

for x in range(3*n):
    BigGraph.append([0]*(3*n))


for i in range(n):
    for j in range(n):
        if grid[i][j] ==' ':
            continue
        elif grid[i][j] == '/':
            BigGraph[3*i][3*j+2]   = 1
            BigGraph[3*i+1][3*j+1] = 1
            BigGraph[3*i+2][3*j]   = 1
        elif grid[i][j] == '\\':
            BigGraph[3*i][3*j]     = 1
            BigGraph[3*i+1][3*j+1] = 1
            BigGraph[3*i+2][3*j+2] = 1


for i in range(3*n):
    for j in range(3*n):
        if BigGraph[i][j] == 0:
            res += 1
            BigGraph = RegionCount(BigGraph,i,j)

print(res)
