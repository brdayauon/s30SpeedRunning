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
            temp = []
            for i in range(size):
                curr = queue.popleft()
                temp.append(curr.val)
                for child in curr.children:
                    queue.append(child)
            res.append(temp)
        return res 