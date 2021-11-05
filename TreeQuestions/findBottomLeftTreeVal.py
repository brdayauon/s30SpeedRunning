# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        queue = deque([root])
        
        while queue:
            size = len(queue)
            leftMost = None
            
            for i in range(size):
                curr = queue.popleft()
                
                if i == 0:
                    leftMost = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return leftMost