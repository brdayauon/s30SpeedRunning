# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        
        stack = [(root, None)]
        while stack:
            curr, parent = stack.pop()
            parents[curr] = parent
            
            if curr.left:
                stack.append((curr.left, curr))
            if curr.right:
                stack.append((curr.right, curr))
        
        queue = deque([(target, 0)])
        seen = set()
        seen.add(target)
        res = []
        while queue:
            size = len(queue)
            
            for i in range(size):
                curr, distance = queue.popleft()
                
                if distance == k:
                    res.append(curr.val)
                    continue
                if curr.left and curr.left not in seen:
                    seen.add(curr.left)
                    queue.append((curr.left, distance+1))
                if curr.right and curr.right not in seen:
                    seen.add(curr.right)
                    queue.append((curr.right, distance+1))
                parent = parents[curr]
                if parent and parent not in seen:
                    seen.add(parent)
                    queue.append((parent, distance+1))
          
        return res
    
    