class Solution(object):


    def Break(self,s,wordDict,memo,dic):
        for word in wordDict:
            if word in s[:len(word)]:
                if not s[len(word):]:
                    temp = memo + [word]
                    s = ''
                    for j in temp:
                        s = s + j + ' '
                    s = s[:-1]
                    dic += [s]
                else:
                    self.Break(s[len(word):],wordDict,memo + [word],dic)




s = "woshinibaba"
wordDict = ["wo","s","shi","ni","hi","ba","baba","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
wordDict.sort(key=lambda i: len(i))
print(wordDict)

memo = []
dic = []
p = Solution()
p.Break(s,wordDict,memo,dic)
print(dic)
print(len(dic))

