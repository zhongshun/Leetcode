# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = [[root.val]]
        cur = [root]
        while cur:
            temp = []
            Nextnode = []
            for i in cur:
                node = cur[i]
                if node.left:
                    l = node.left
                    Nextnode.append(l)
                    temp.append(l.val)
                if node.right:
                    r = node.right
                    Nextnode.append(r)
                    temp.append(r.val)
            cur = Nextnode
            res.append(temp)
        return res