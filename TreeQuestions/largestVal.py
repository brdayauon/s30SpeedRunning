# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        #lets do bfs
        res=[]
        if not root:
            return res
        
        queue = deque([root])
        
        while queue:
            size = len(queue)
            mx = float(-inf)
            for i in range(size):
                curr = queue.popleft()
                
                mx = max(mx, curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            res.append(mx)
        return res