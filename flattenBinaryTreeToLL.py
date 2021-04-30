# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        stack = [root]
        prev = None        
        #preorder
        while stack:
            curr = stack.pop()
            #check neighbors
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                
            if prev:
                prev.right = curr
                prev.left = None
                curr.left = None
                
            prev = curr
