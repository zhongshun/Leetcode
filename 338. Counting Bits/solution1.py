def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    dict = {}
    dict[0] = 0
    dict[1] = 1
    for i in range(num+1):
        if i not in dict:
            dict[i] = dict[i<<2] + i%2
    return dict

def int2Bits(num):
    res = 0
    while num > 0:
        res = res + num%2
        num = int(num/2)
    return res
res = [0]
for i in range(5):
    res.append(-1)
print(res)
