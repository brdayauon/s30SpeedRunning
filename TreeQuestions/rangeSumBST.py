# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        #level order
        total = 0
        if not root:
            return 0
        
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                
                if curr.val >= low and curr.val <= high:
                    total += curr.val 
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
        return total
#         #preorder traversal
#         total = 0
#         if not root:
#             return 0 
        
#         stack = [root]
#         while stack:
#             curr = stack.pop()
            
#             if curr.val >= low and curr.val <= high:
#                 total += curr.val
#             if curr.left:
#                 stack.append(curr.left)
#             if curr.right:
#                 stack.append(curr.right)
                
#         return total
        
        
#         #inorder traversal
#         total = 0
#         if not root:
#             return 0
        
#         stack = []
        
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left 
            
#             root = stack.pop()
            
#             if root.val >= low and root.val <= high:
#                 total += root.val 
            
#             root = root.right 
        
#         return total