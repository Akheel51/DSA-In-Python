# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lh=self.height(root.left)
        rh=self.height(root.right)
        if lh-rh>1 or rh-lh>1:
            return False
        leftside=self.isBalanced(root.left)
        rightside=self.isBalanced(root.right)
        if leftside and rightside:
            return True
        else:
            return False
    def height(self,root):
        if root is None:
            return 0
        else:
            return 1+max(self.height(root.left),self.height(root.right))
        