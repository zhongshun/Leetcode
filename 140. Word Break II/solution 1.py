class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        memo={}
        def dp(i):
            if (i) not in memo:
                ans = False
                for word in wordDict:
                    if word == s[i:i+len(word)]:
                        if s[i:] == word:
                            ans = True
                            break
                        else:
                            ans = dp(i + len(word))
                            if ans:
                                break
                memo[i] = ans
            return memo[i]

        return dp(0)

