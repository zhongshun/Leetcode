class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isPalindrome(s):
            for i in range(len(s) >> 1):
                if s[i] != s[-i - 1]:
                    return False
            return True
        self.dict = {}
        def DP(i,j):
            if (i,j) in self.dict[(i,j)]:
                return self.dict[(i,j)]
            if i == j:
                self.dict[(i, j)] = s[i]
                return self.dict[(i,j)]
            if s[i] == s[j]:
                self.dict[(i, j)] = s[i] + DP(i-1,j-1) + s[j]
                DP(i,j) = s[i] + DP(i-1,j-1) + s[j]
dict = {}
dict[(1,2)] = 11
print(dict)