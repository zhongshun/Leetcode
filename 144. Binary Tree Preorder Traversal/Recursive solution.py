# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def Traversal(root,L):
        Head = root
        if Head.left:
            p = Head.left
            L.append(p.val)
            Traversal(p,L)
        if Head.right:
            p = Head.right
            L.append(p.val)
            Traversal(p,L)
        return
    if root:
        L = [root.val]
        Traversal(root,L)
        return L
    else:
        return []


p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p1.right = p2
p2.left = p3

print(preorderTraversal(p1))
