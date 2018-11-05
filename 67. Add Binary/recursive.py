class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def addB(a,b):
            if len(a) == 0: return b
            if len(b) == 0: return a
            if a[-1] == '0' and b[-1] == '0':
                return addB(a[:len(a)-1],b[:len(b)- 1]) + '0'
            elif a[-1] != b[-1]:
                return addB(a[:len(a)-1],b[:len(b)- 1]) + '1'
            else:
                return addB(addB(a[:len(a)-1],b[:len(b)- 1]),'1') + '0'
        return addB(a,b)



a = "10101"
b =   "101"
p = Solution()
print(p.addBinary(a,b))
