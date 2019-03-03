
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if not t1 and not t2:
        return None
    elif not t2:
        return t1
    elif not t1:
        return t2
    else:
        t1.val = t1.val + t2.val
        t1.left = mergeTrees(t1.left,t2.left)
        t1.right = mergeTrees(t1.right,t2.right)

    return

T1 = TreeNode(1)
T2 = TreeNode(3)
T3 = TreeNode(2)
T4 = TreeNode(5)
T1.left = T2
T1.right = T3
T2.left = T4

P1 = TreeNode(2)
P2 = TreeNode(1)
P3 = TreeNode(3)
P4 = TreeNode(4)
P5 = TreeNode(7)

P1.left = P2
P1.right = P3
P2.right = P4
P3.right = P5


L = mergeTrees(T1, P1)


