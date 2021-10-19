"""
TC: 
SC: 

Given a binary tree.. we need to check if it is height balanced. That is when a binary tree where the left and right subtrees
differ in height by no more than one..

How we can do this is from the root node.. check the left and right subtrees and see if it is height balanced. We can do this recursively.
Where we go the the leaf nodes and check if they are height balanced. 
"""

def isHeightBalanced(root):
    
    def helper(root):
        if not root:
            return [True,0]
        
        leftTree = helper(root.left)
        rightTree = helper(root.right)

        if leftTree[0] == True and rightTree[0] == True and abs(leftTree[1]-rightTree[1]) <= 1:
            return [True,max((leftTree[1],rightTree[1])+1)]
        else:
            return [False,max((leftTree[1],rightTree[1])+1)]
    return helper(root)[0] == True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return [True,0]

            leftTree = helper(root.left)
            rightTree = helper(root.right)

            if leftTree[0] == True and rightTree[0] == True and abs(leftTree[1]-rightTree[1]) <= 1:
                return [True,max(leftTree[1],rightTree[1])+1]
            else:
                return [False,max(leftTree[1],rightTree[1])+1]
        return helper(root)[0] == True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return [True,0]

            leftTree = helper(root.left)
            rightTree = helper(root.right)

            balanced = leftTree[0] == True and rightTree[0] == True and abs(leftTree[1]-rightTree[1]) <= 1

            return [balanced, max(leftTree[1],rightTree[1])+1]
        return helper(root)[0] == True