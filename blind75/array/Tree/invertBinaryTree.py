# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            temp = curr.left 
            curr.left = curr.right
            curr.right = temp
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                
        return root