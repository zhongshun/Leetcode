import math
def groupAnagrams(strs):
    dic = {}
    for i in range(len(strs)):
        s = strs[i]
        a = list(s)
        a.sort()
        a = str(a)
        if a not in dic:
            dic[a] = [s]
        else:
            dic[a] =dic[a] + [s]
    res = []
    for s in dic:
        res = res + [dic[s]]
    return res





    print(dic)


Input = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(Input)
