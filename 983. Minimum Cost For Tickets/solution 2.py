days = [1,4,6,7,8,20]
costs = [2,7,15]

def mincostTickets(days, costs):
    dp = []
    for i in range(days[-1]+1):
        dp.append(0)

    for k in range(days[-1]+1):
        if k in days:
            dp[k] = min(dp[max(0,k-1)] + costs[0], dp[max(0,k-7)] + costs[1], dp[max(0,k-30)] + costs[2])
        else:
            dp[k] = dp[k-1]
    print(dp)
    return dp[-1]

print(mincostTickets(days,costs))
