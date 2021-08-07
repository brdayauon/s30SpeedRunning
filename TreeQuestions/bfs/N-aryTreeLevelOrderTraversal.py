"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            currArr = []
            for i in range(size):
                curr = queue.popleft()                
                currArr.append(curr.val)
                
                children = curr.children 
                for j in children:
                    queue.append(j)
                    
            res.append(currArr)
            
        return res
