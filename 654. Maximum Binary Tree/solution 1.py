class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Devide(nums,P,LorR):
    pointer = TreeNode(max(nums))
    if LorR == 1:
        P.left = pointer
    else:
        P.right = pointer
    i = nums.index(max(nums))

    if nums[:i]:
        Devide(nums[:i], pointer, 1)
    if nums[i+1:]:
        Devide(nums[i+1:],pointer,2)
    if not nums[:i] and not nums[i+1:]:
        return

nums = [3,2,1,6,0,5]
P = TreeNode(max(nums))
i = nums.index(max(nums))
if nums[:i]:
    Devide(nums[:i],P,1)
if nums[i+1:]:
    Devide(nums[i+1:],P,2)


