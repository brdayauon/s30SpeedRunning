# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.hm = {}
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.setParents(root, None)
        queue = deque([target])
        seen = set()
        seen.add(target)
        dist = 0
        while queue:
            size = len(queue)
            
            if dist == k:
                res = []
                for node in queue:
                    res.append(node.val)
                return res
            
            for i in range(size):
                curr = queue.popleft()
                seen.add(curr)
                
                if curr.left and curr.left not in seen:
                    seen.add(curr.left)
                    queue.append(curr.left)
                if curr.right and curr.right not in seen:
                    seen.add(curr.right)
                    queue.append(curr.right)
                    
                parent = self.hm[curr]
                if parent and parent not in seen:
                    seen.add(parent)
                    queue.append(parent)
            
            dist += 1
                
        return []
        
    
    def setParents(self,node, parent):
        if node:
            self.hm[node] = parent
            self.setParents(node.left, node)
            self.setParents(node.right, node)