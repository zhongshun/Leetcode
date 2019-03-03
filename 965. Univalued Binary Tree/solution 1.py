
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





def IsUni(root,value):
    if root.val != value:
        return False
    if root.left:
        if not IsUni(root.left,value):
            return False
    if root.right:
        if not IsUni(root.right,value):
            return False
    return True

p = TreeNode(0)
print(p.val)
print(IsUni(p,p.val))
