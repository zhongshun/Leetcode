class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def CompareLeftRight(Left,Right):
            if not Left and not Right:
                return True
            elif not Left or not Right:
                return False
            else:
                return Left.val == Right.val and CompareLeftRight(Left.left,Right.right) and CompareLeftRight(Left.right,Right.left)
