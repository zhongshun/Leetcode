class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = max(nums)
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                if sum(nums[i:j]) > r:
                    r = sum(nums[i:j])

        return r

nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
p = Solution()
print(p.maxSubArray(nums))
