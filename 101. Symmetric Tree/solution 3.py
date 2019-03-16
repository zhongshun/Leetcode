class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        Children = [root]
        while Children:
            L = len(Children)>>1
            for i in range(L):
                left = Children[i]
                Right = Children[-1-i]
                if not left and not Right:
                    continue
                if not left or not Right:
                    return False
                if left.val != Right.val:
                    return False
            Next = []
            for node in Children:
                if node:
                    Next.append(node.left)
                    Next.append(node.right)
            Children = Next

        return True

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(2)
t4 = TreeNode(3)
t5 = TreeNode(3)

t1.left = t2
t1.right = t3

t2.right = t4
t3.right = t4



p = Solution()
print(p.isSymmetric(t1))
