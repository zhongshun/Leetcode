A = [3,1,2,4]
class Solution:
    def sumSubarrayMins(self, A):
        res = 0
        stack = []  #  non-decreasing
        A = [-9999999999] + A + [-9999999999]
        for i,num in enumerate(A):
            while stack and A[stack[-1]] > num:
                cur = stack.pop()
                res += A[cur]*(i-cur)*(cur-stack[-1])
            stack.append(i)
        return res

p = Solution()
print(p.sumSubarrayMins(A))
