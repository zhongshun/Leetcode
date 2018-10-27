def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    nums.sort()
    L = 1
    MaxL = 1
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 1:
            L = L + 1
        elif nums[i+1] - nums[i] == 0:
            continue
        else:
            L = 1
        if L > MaxL:
            MaxL = L
    return MaxL

Input = [1,2,0, 1]
print(longestConsecutive(Input))
