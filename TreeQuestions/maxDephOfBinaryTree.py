# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #dfs
        if not root:
            return 0
        
        stack = [(1, root)]
        mx = 0
        while stack:
            depth, curr = stack.pop()
            mx = max(mx, depth)
            if curr.left:
                stack.append((depth+1, curr.left))
            if curr.right:
                stack.append((depth+1, curr.right))
                
        return mx