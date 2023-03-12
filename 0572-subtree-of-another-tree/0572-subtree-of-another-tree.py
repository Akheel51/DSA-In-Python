# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        def identical(root,subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val==subroot.val:
                return identical(root.left,subroot.left) and identical(root.right,subroot.right)
            return False
        
        if not root:
            return False
        if not subroot:
            return True
        if identical(root,subroot):
            return True
        return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)
        