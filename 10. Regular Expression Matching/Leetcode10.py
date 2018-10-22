
#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
def ismatch(s, p):
    memo = {}
    def dp(i, j):
        if (i,j) not in memo:
            if j == len(p):
                ans = i == len(s)
            else:
                first_match = bool(s[i]) and p[j] in {s[i], '.'}
                if len(s[i:]) < 3:
                    ans = first_match
                if len(p[j:]) > 2 and p[j+1] == '*':
                    ans =  dp(i,j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)
            memo[i, j] = ans
        return memo[i, j]
    return dp(0,0)

s = "aa"
p= "a*"

s = s + '__'
p = p + '__'
print(ismatch(s, p))


