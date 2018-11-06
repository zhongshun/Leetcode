class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        Height = height
        Height2 = [num for num in Height]
        H1 = Height.index(max(Height))
        Height2[H1] = 0
        H2 = Height2.index(max(Height2))
        if H1 == H2:
            return 0


        V = (abs(H1-H2)-1)*Height[H2]
        for i in range(min(H1,H2)+1, max(H1,H2)):
            V = V - Height[i]
            if V <= 0:
                break
        if V <= 0:
            V = 0
        return V + self.trap(height[:min(H1,H2)+1]) + self.trap(height[max(H1,H2):])

height = [5,3,4,6,6,8,4,4]
#height = [3, 2, 1, 2, 1]
p = Solution()
print(p.trap(height))
