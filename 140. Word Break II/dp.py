class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.help(s,wordDict,{})

    def help(self,s,wordDict,memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if word != s[:len(word)]:
                continue
            if len(s) == len(word):
                res.append(word)
            else:
                rest = self.help(s[len(word):],wordDict,memo)
                for item in rest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res





s = "aaaaaaa"
wordDict = ["aaaa","aa","a"]
p = Solution()
dic = p.wordBreak(s,wordDict)
print(dic)
print(len(dic))
