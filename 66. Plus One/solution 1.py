class Solution(object):
    def plusOne(self,digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        times = 1
        res = 0
        if not digits:
            return 0
        while digits:
            res += digits[-1]*times
            times *= 10
            digits.pop()
            result = [int(i) for i in str(res+1)]
        return result

Input = [9,9,9,9,9]
p = Solution()
print(p.plusOne(Input))
