# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        #inorder traversal
        stack = []
        prev = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            
            root = stack.pop()
            #make sure its in order
            if root.val <= prev:
                return False
            prev = root.val

            root = root.right 
        
        return True