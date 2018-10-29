class Solution(object):
    def isMatch(self,s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        '?' Matches any single character.
        '*' Matches any sequence of characters (including the empty sequence).
        """
        if s and not p:
            return False
        elif not s:
            if not p:
                return True
            elif p[0] == '*':
                return self.isMatch(s,p[1:])
            else:
                return False
        elif s == p:
            return True
        elif p[0] == '*' and len(p) == 1:
            return True

        elif s[0] == p[0] or p[0] == '?':
            return self.isMatch(s[1:],p[1:])
        elif p[0] == '*':
            return self.isMatch(s[1:],p) or self.isMatch(s,p[1:])

        return False

s = "mississippi"
p = "m??*ss*?i*pi"
A = Solution()
print(A.isMatch(s,p))
