"""
TC: O(N)
SC: O(N)

Put to_delete into a set so the lookup here is O(1)
Perform a dfs on the root node. 
    - TO traverse.. check if there is a left/right node 
        - add it to the stack because we need to process those
        - At the same time check if the left/right node is in the set then we have to delete the pointers accordingly.
    - If we are on the node that is in the set..
        - We have to make sure the left/right nodes are not in the set.. if they are not then you know that they have to become their own nodes so append it to the result
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        stack = [root]
        seen = set(to_delete)
        res = []
        
        while stack:
            curr = stack.pop()
            
            if curr.val in seen:
                if curr.left and curr.left.val not in seen:
                    res.append(curr.left)
                if curr.right and curr.right.val not in seen:
                    res.append(curr.right)
                    
            if curr.left:
                stack.append(curr.left)
                if curr.left.val in seen:
                    curr.left = None
            if curr.right:
                stack.append(curr.right)
                if curr.right.val in seen:
                    curr.right = None
                    
        if root.val not in seen:
            res.append(root)
        return res
