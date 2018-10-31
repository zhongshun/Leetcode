class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        #wordDict.sort(key=lambda i: len(i))
        return self.help(s,wordDict,{})

    def help(self,s,wordDict,memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        res = []
        for word in wordDict:
            if word != s[:len(word)]:
                continue
            if not s[len(word):]:
                res.append(word)
            else:
                ans = self.help(s[len(word):],wordDict,memo)
                for temp in ans:
                    temp = word + ' ' + temp
                    res.append(temp)
        memo[s] = res
        return res



s = "aaaaaaa"
wordDict = ["aaaa","aa","a"]
p = Solution()
dic = p.wordBreak(s,wordDict)
print(dic)
print(len(dic))
