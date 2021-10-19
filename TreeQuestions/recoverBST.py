# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        prev = None
        firstNode = secondNode = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop() 
            if prev == None:
                prev = root 
            if prev and root.val < prev.val:
                firstNode = root
                if not secondNode:
                    secondNode = prev
                    
            prev = root 
            root = root.right 
        temp = firstNode.val 
        firstNode.val = secondNode.val 
        secondNode.val = temp