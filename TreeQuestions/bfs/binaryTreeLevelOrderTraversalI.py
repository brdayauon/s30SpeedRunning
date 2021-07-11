from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        stack = []
        while queue:
            size = len(queue)
            lvl = []
            for i in range(size):
                curr = queue.popleft()
                
                lvl.append(curr.val)
                
                if i == size-1:
                    stack.append(lvl)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        res = []
        while stack:
            res.append(stack.pop())
        
        return res