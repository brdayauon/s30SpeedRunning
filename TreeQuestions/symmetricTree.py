"""
TC: O(N)
SC: O(N)

Given a binary tree... we have to check if it is a mirror of itself around the center.. 
Since we have to go around its root.. we should check the left/right nodes of the root and downward. 
Can do this BFS dfs... 
    - Initialize stack and put in the leftNode and rightNode of root. 
    - Process stack
        - pop Twice from stack.. leftNode..RightNode.. 
        - Check if they are the same.. if they are not then return False .
            - Check values are the same.. if both are null .. if one of them is null.. blah blah
        - since it is mirror of each other.. how we check the equality is based on how we put it in the stack/queue.
        We can do it in this order.. 
        stack.append(leftNode.left)
        stack.append(rightNode.right)
        stack.append(leftNode.right)
        stack.apend(rightNode.left)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        
        stack.append(root.left)
        stack.append(root.right)
        
        while stack:
            leftTree = stack.pop()
            rightTree = stack.pop()
            
            if not leftTree and not rightTree:
                continue
            if (not leftTree or not rightTree) or leftTree.val != rightTree.val:
                return False
            
            stack.append(leftTree.left)
            stack.append(rightTree.right)
            stack.append(rightTree.left)
            stack.append(leftTree.right)
            
        return True