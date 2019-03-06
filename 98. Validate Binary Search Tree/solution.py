
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def DFS(root,minimun,maximum):
            if not root:
                return True

            if root.left:
                L = root.left
                if L.val < root.val and L.val <= maximum and L.val >= minimun:
                    if not DFS(L, max(L.val, minimun), maximum):
                        return False
                else:
                    return False

            if root.right:
                R = root.right
                if R.val > root.val and R.val >= minimun and R.val <= maximum:
                    if not DFS(R, minimun, min(R.val,maximum)):
                        return False
                else:
                    return False

            return True

        return DFS(root,-1000000, 10000000)




t1 = TreeNode(3)
t2 = TreeNode(1)
t3 = TreeNode(5)
t4 = TreeNode(0)
t5 = TreeNode(2)
t6 = TreeNode(4)
t7 = TreeNode(6)

t1.left = t2
t1.right = t3

t2.left = t4
t2.right = t5

t3.left = t6
t3.right = t7




P1 = Solution()
print(P1.isValidBST(t1))
