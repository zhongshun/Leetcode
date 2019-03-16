A = [3,1,2,4]
class Solution(object):
    def sumSubarrayMins(self, A):
        self.res = 0
        def FindSubMin(A):
            if not A:
                return 0
            L = len(A)
            i = A.index(min(A))
            self.res += A[i]*(i+1)*(L-i)
            FindSubMin(A[:i])
            FindSubMin(A[i+1:])
        FindSubMin(A)
        return self.res

p = Solution()
print(p.sumSubarrayMins(A))
