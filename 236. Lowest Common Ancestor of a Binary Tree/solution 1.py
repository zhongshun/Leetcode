class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def GetPosition(root,node, list):
            if not root:
                return False

            if root != node:
                if GetPosition(root.left, node, list):
                    list.append(root)
                    return True
                elif GetPosition(root.right, node, list):
                    list.append(root)
                    return True
            else:
                list.append(root)
                return True

        listA = []
        GetPosition(root,p, listA)
        for nodeA in listA:
            print(nodeA.val)

        listB = []
        GetPosition(root,q, listB)
        for nodeB in listB:
            print(nodeB.val)

        list =  [val for val in listA if val in listB]
        for node in list:
            print(node.val)

