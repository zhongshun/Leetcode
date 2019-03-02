s = "pwwkew"
dp = [1]*len(s)
posdict = {s[0]: 0}
longest = 1
for i in range(1, len(s)):
    if s[i] in posdict:
        dp[i] = min(dp[i-1]+1, i-posdict[s[i]])
    else:
        dp[i] = dp[i-1] + 1
    posdict[s[i]] = i
    if longest < dp[i]:
        longest = dp[i]
print(longest)
