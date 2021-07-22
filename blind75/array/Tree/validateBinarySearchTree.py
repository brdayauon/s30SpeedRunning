# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #inorder
        stack = []
        prev = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            
            root = stack.pop()
            
            if root.val > prev:
                prev = root.val 
            else:
                return False
            
            root = root.right
        return True