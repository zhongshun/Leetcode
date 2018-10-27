def lengthOfLastWord(s):
    if not s:
        return 0
    res = 0
    s_list = list(s)
    while s_list[-1] == ' ':
        s_list.pop()
        if not s_list:
            return 0

    while s_list and s_list[-1] != ' ':
        res = res + 1
        s_list.pop()
    return res

s = " "
word = s.split()
print(word)


