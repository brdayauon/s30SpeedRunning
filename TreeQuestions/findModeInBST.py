# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hm = {}
        
        stack = [root]
        
        while stack:
            curr = stack.pop()
            
            if curr.val not in hm:
                hm[curr.val] = 1
            else:
                hm[curr.val] += 1
                
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        mx = float('-inf')
        res = set()
    
        for k,v in hm.items():
            if mx == v:
                res.add(k)
            elif mx < v:
                res = set()
                res.add(k)
                mx = v
        return res
                