class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while True:
            if i >= len(nums) - 2:
                break

            if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                nums.remove(nums[i+2]);
            else:
                i = i + 1
        return len(nums)


nums = [1,1,1,2,2,3]
p = Solution()
print(p.removeDuplicates(nums))
