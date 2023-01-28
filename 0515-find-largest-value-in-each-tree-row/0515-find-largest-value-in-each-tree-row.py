# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        q = deque([root])
        
        if root:
        
            while q:

                cur_max = -float('inf')

                for _ in range(len(q)):

                    cur = q.popleft()

                    cur_max = max(cur.val,cur_max)

                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)

                ans.append(cur_max)

        return ans
        