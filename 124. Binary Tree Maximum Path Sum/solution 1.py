class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0

def ChildNodeMaxValue(root):
    if not root:
        return 0
    currentmaxL = currentmaxR = summax = root.val
    if root.left:
        currentmaxL = currentmaxL + ChildNodeMaxValue(root.left)
        summax = max(summax,currentmaxL)
    if root.right:
        currentmaxR = currentmaxR + ChildNodeMaxValue(root.right)
        summax = max(summax,currentmaxR)
    return summax


def ExploreTree(root,stack):
    stack.append(root)
    if root.left:
        ExploreTree(root.left, stack)
    if root.right:
        ExploreTree(root.right, stack)
    return root

t1 = TreeNode(-10)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5
stack = []

###################################
ExploreTree(t1,stack)

res = []
pValue = []
for p in stack:
    pValue.append(p.val)
    res.append(max(0,ChildNodeMaxValue(p.left)) + max(0,ChildNodeMaxValue(p.right)) + p.val)
print(pValue)
print(res)
