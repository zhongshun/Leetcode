class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return 1
a = "10101"
b =   "101"

la = len(a)
lb = len(b)
if la >= lb:
    long = a
    short = b
else:
    long = b
    short = a
add = '0'
res=''
for i in range(len(short)):
    if add == '0':
        if long[-1-i] == '0' and short[-1-i] == '0':
            res = '0' + res
            add = '0'
        elif long[-1-i] == '1' and short[-1-i] == '1':
            res = '0' + res
            add = '1'
        else:
            res = '1' + res
            add = '0'
    else:
        if long[-1-i] == '0' and short[-1-i] == '0':
            res =  '1' + res
            add = '0'
        elif long[-1-i] == '1' and short[-1-i] == '1':
            res = '1' + res
            add = '1'
        else:
            res = '0' + res
            add = '1'
for j in range(len(long) - len(short)):
    if long[-1-i-j-1] == add:
        if add == '1':
            res = '0' + res
            add = '1'
        else:
            res = '0' + res
            add = '0'
    else:
        res = '1' + res
        add = '0'
if add == '1':
    res = '1' + res
print(res)
