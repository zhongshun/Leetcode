# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def moves(node):
            if not node:
                return 0
            else:
                L = moves(node.left)
                R =  moves(node.right)
                self.ans += abs(L) + abs(R)
                return node.val - 1 + L + R
        moves(root)
        return self.ans

p1 = TreeNode(3)
p2 = TreeNode(0)
p3 = TreeNode(0)
p4 = TreeNode(0)
p1.left = p2
p1.right = p3


X = Solution()
print(X.distributeCoins(p1))

