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
        self.maxValue = - 1111110
        def ChildNodeMaxValue(root):
            if not root: return 0
            L = max(ChildNodeMaxValue(root.left),0)
            R = max(ChildNodeMaxValue(root.right),0)
            summax = max(root.val + L, root.val + R)
            self.maxValue = max(self.maxValue, root.val + L + R)
            return summax

        ChildNodeMaxValue(root)
        return self.maxValue

t1 = TreeNode(5)
t2 = TreeNode(4)
t3 = TreeNode(8)
t4 = TreeNode(11)
t5 = TreeNode(13)
t6 = TreeNode(4)
t7 = TreeNode(7)
t8 = TreeNode(2)
t9 = TreeNode(1)

t1.left = t2
t1.right = t3
t2.left = t4
t3.left = t5
t3.right = t6
t4.left  = t7
t4.right = t8
t6.right = t9


###################################
p = Solution()
res = p.maxPathSum(t1)
print(res)
