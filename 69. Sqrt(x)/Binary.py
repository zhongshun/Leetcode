class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1

        left, right = 0,x
        while True:
            mid = int((left + right)/2)
            if mid*mid <= x and (mid + 1)*(mid + 1) > x:
                return mid
            elif mid*mid > x:
                right = mid
            else:
                left = mid
p = Solution()
print(p.mySqrt(10))
