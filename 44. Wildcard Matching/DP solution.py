class Solution(object):
    def isMatch(self,s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        '?' Matches any single character.
        '*' Matches any sequence of characters (including the empty sequence).
        """
        memo = {}
        s = s + '_'
        p = p + '_'
        def DP(i,j):
            if (i,j) not in memo:
                first_match = i < len(s) and p[j] in {s[i],'?'}
                if s[i:] == p[j:]:
                    ans = True
                elif not s[i:]:
                    if p[j] == '*':
                        ans = DP(i,j+1)
                    else:
                        ans = False

                elif first_match:
                    ans = DP(i+1,j+1)
                elif s[i:] and p[j] == '*':
                    ans = DP(i,j+1) or DP(i+1,j)
                else:
                    ans = False
                memo[i,j] = ans
            return memo[i,j]
        return DP(0,0)

s = "mississippi"
p = "m??*ss*?i*pi"
A = Solution()
print(A.isMatch(s,p))




