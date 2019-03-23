def temp(s, l, r):
    while l -1 >= 0 and r + 1 < len(s) and s[l-1] == s[r + 1]:
        l = l - 1
        r = r + 1
    return s[l:r + 1]

s = "ccc"

maxlength = 0
maxletter = ""

for i in range(len(s)):

    temp1 = temp(s, i, i)
    if len(temp1) > maxlength:
        maxletter = temp1
        maxlength = len(maxletter)

    if i + 1 < len(s):
        if s[i] == s[i+1]:
            temp2 = temp(s, i, i + 1)
            if len(temp2) > maxlength:
                maxletter = temp2
                maxlength = len(maxletter)



print(maxletter)
#Output: "bab"
