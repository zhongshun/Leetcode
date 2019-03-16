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
            if Left.val != Right.val:
                return False
            L1 = Left.left
            R1 = Left.right

            L2 = Right.left
            R2 = Right.right

            if L1 and L2 and R1 and R2:
                if [L1.val, R1.val] == [R2.val, L2.val]:
                    if CompareLeftRight(L1,R2) and CompareLeftRight(R1,L2):
                        return True
                    else:
                        return False
            elif L1 and not R1 and not L2 and R2:
                if L1.val == R2.val:
                    if CompareLeftRight(L1, R2):
                        return True
                    else:
                        return False
            elif not L1 and R1 and L2 and not R2:
                if R1.val == L2.val:
                    if CompareLeftRight(R1,L2):
                        return True
                    else:
                        return False
            elif not L1 and not L2 and not R1 and not R2:
                return True
            return False

        return CompareLeftRight(root.left,root.right)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(3)
t5 = TreeNode(4)
t6 = TreeNode(4)
t7 = TreeNode(3)

t1.left = t2
t1.right = t3


p = Solution()
print(p.isSymmetric(t1))

