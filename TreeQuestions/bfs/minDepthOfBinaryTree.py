# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([([root, 1])])
        mn = float('inf')
        
        while queue:
            node, depth = queue.popleft()
            
            if not node.left and not node.right:
                mn = min(mn, depth)
                
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
                
        return mn

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root,1)])
        mn = float('inf')
        while queue:
            curr, depth = queue.popleft()
            
            if not curr.left and not curr.right:
                mn = depth
                break
                
            if curr.left:
                queue.append((curr.left, depth+1))
            if curr.right:
                queue.append((curr.right, depth+1))
        return mn