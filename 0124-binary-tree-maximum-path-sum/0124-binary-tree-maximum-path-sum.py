# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float("-inf")
        def postorder(root):
            if not root:  
                return 0
            left_val= max(0, postorder(root.left)) 
            right_val=max(0, postorder(root.right))
            curr=(root.val + left_val + right_val)
            self.ans = max(self.ans,curr)
            return max((root.val + left_val), (root.val + right_val))
        postorder(root)
        return self.ans
