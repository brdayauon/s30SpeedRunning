# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        stack = []
        dist = float('inf')
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
                
            root = stack.pop()
            
            if prev != None:
                dist = min(dist, abs(root.val-prev))
            
            prev = root.val 
            
            root = root.right 
        return dist