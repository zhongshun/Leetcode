import math
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return nums.index(max(nums))
        left = 0
        right = len(nums)
        i = int((left + right)/2)
        while True:
            if i - 1 == -1 and nums[i] > nums[i+1]:
                return i
            elif i + 1 == len(nums) and nums[i] > nums[i-1]:
                return i
            elif nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return i
            elif nums[i] < nums[i+1]:
                left = i
                i = int((i+right)/2)
            else:
                right = i
                i = int((i+left)/2)
nums =  [1,2,3,1]
p = Solution()
print(p.findPeakElement(nums))
