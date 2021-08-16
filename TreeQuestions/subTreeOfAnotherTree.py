# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        
        while queue:
            curr = queue.pop()
            
            if self.isSame(curr, subRoot):
                return True
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                
        return False
    
    def isSame(self, rootA, rootB):
        if not rootA and not rootB:
            return True
        
        if not rootA or not rootB:
            return False
        if rootA.val != rootB.val:
            return False
        else:
            return self.isSame(rootA.left, rootB.left) and self.isSame(rootA.right, rootB.right)
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         stack = [root]
        
#         while stack:
#             curr = stack.pop()
            
#             if self.isSame(curr, subRoot):
#                 return True
            
#             if curr.left:
#                 stack.append(curr.left)
#             if curr.right:
#                 stack.append(curr.right)
                
#         return False
    
#     def isSame(self, rootA, rootB):
#         if not rootA and not rootB:
#             return True
        
#         if not rootA or not rootB:
#             return False
#         if rootA.val != rootB.val:
#             return False
#         else:
#             return self.isSame(rootA.left, rootB.left) and self.isSame(rootA.right, rootB.right)
        
        
        