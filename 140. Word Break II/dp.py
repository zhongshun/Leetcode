class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp_record = {}
        wordDict.sort(key=lambda i: len(i))
        def dp(i):
            if (i) not in dp_record:
                sx = s[i:]
                for word in wordDict:
                    if word in sx[:len(word)]:
                        if not sx[len(word):]:
                            dp_record[i] = [word]
                        else:
                            if dp(i+len(word)):
                                dp_record[i] = [word] + dp_record[i+len(word)]

            return dp_record[i]

        return dp(0)





s = "aaaaaaa"
wordDict = ["aaaa","aa","a"]
p = Solution()
dic = p.wordBreak(s,wordDict)
print(dic)
print(len(dic))
