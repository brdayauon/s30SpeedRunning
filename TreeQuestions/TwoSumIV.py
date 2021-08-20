# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hm = {}
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            if root.val in hm:
                return True
            else:
                hm[k-root.val] = 1
            
            root = root.right
        return False