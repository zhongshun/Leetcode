"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def DFsearch(list, root):
            if root.children:
                for p in root.children:
                    DFsearch(list, p)
            list.append(root.val)
        if not root:
            return []
        res = []
        DFsearch(res,root)
        return res

