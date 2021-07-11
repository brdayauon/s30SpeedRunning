# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res 
        
        queue = deque([root])
        cols = deque([0])
        rows = deque([0])
        hm = {}
        mn = mx = 0
        while queue:
            node = queue.popleft()
            row = rows.popleft()
            col = cols.popleft()
            
            mn = min(mn,col)
            mx = max(mx, col)
            
            if col not in hm:
                hm[col] = []
                
            hm[col].append((row,node.val))
            
            if node.left:
                queue.append(node.left)
                cols.append(col - 1)
                rows.append(row+1)
            if node.right:
                queue.append(node.right)
                cols.append(col+1)
                rows.append(row+1)

        # for key, val in hm.items():
        #     res.append(val)
        for i in range(mn,mx+1):
            res.append([lst for row, lst in sorted(hm[i])])
            
        return res