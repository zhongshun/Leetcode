Input=[[0,0],[1,1],[0,0]]


dp = []
for i in range(len(Input)):
    dp = dp + [len(Input[0])*[0]]



for x in range(len(Input[0])):
    if Input[0][x] == 0:
        dp[0][x] = 1
    else:
        break


for y in range(len(Input)):
    if not Input[y][0]:
        dp[y][0] = 1
    else:
        break

for y in range(1,len(Input)):
    for x in range(1,len(Input[0])):
        if Input[y][x] == 1:
            dp[y][x] == 0
        else:
            dp[y][x] = dp[y][x-1] + dp[y-1][x]
print(dp)








