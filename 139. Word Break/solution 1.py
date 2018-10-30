def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    for word in wordDict:
        if word in s[:len(word)]:
            if not s[len(word):]:
                return True
            else:
                if wordBreak(s[len(word):],wordDict):
                    return True
    return False




s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s,wordDict))
