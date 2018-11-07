class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height)-1

        maxl = 0
        maxr = 0
        res = 0
        while l<r:
            maxl = max(maxl,height[l])
            maxr = max(maxr,height[r])
            if maxl < maxr:
                res += maxl - height[l]
                l += 1
            else:
                res += maxr - height[r]
                r -= 1
        return res




#height = [5,3,4,6,6,8,4,4]
#height = [3, 2, 1, 2, 1]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
p = Solution()
print(p.trap(height))
