class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator%denominator:
            res = numerator/denominator
            return str(res)
        else:
            return  1

numerator = -50
denominator = 8
if numerator*denominator >= 0:
    sign = 1
else:
    sign = -1
    numerator = abs(numerator)
    denominator = abs(denominator)

num = []
remain = []
i = 0
repeat_start = 0
repeat_end = 0
num.append(int(numerator/denominator))
remain.append(numerator - num[0]*denominator)
while True:
    i = i + 1
    numerator = remain[i-1]*10
    num.append(int(numerator/denominator))
    remain.append(numerator - num[i]*denominator)
    if remain[i] == 0:
        break
    if remain[i] in remain[1:i]:
        for k in range(1,i):
            if remain[i] in remain[k:i]:
                if num[remain[k:i].index(remain[i]) + k] == num[i]:
                    repeat_start = remain[k:i].index(remain[i]) + k
                    repeat_end = i
                    break
            else:
                break
    if repeat_start:
        break
print(num)
print(remain)
print(repeat_start,repeat_end)
s = ''
if repeat_start == 0:
    s = str(num[0]) + '.'
    for j in range(1,len(num)):
        s += str(num[j])
else:
    s = str(num[0]) + '.'
    for j in range(1,repeat_start):
        s += str(num[j])
    s += '('
    for j in range(repeat_start,repeat_end):
        s += str(num[j])
    s += ')'


while '.' in s and (s[-1] == '0' or s[-1] == '.'):
    s = s[:len(s)-1]
if sign == -1:
    s = '-' + s

print(s)
