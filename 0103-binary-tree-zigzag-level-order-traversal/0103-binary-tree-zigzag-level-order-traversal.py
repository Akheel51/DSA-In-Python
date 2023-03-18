# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
    
        queue = [root]
        result = []
        level = 0
    
        while queue:
            level_nodes = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                level_nodes.reverse()
            result.append(level_nodes)
            level += 1
    
        return result
        