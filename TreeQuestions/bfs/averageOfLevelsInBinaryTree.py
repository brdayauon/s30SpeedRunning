from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        #do lvl order
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            size = len(queue)
            total = 0
            for i in range(size):
                curr = queue.popleft()
                
                total += curr.val 
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(total/size)
        
        return res