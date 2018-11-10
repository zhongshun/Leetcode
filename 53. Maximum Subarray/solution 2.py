class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        currmax = summax = nums[0]
        for num in nums[1:]:
            currmax = max(num,currmax + num)
            summax = max(summax,currmax)
        return summax



nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
p = Solution()
print(p.maxSubArray(nums))
