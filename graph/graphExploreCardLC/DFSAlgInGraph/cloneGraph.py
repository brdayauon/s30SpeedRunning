""" 
1-2-3-4
1'-
hm = {1:1'}  stack = [1]
curr = 1  stack=[]
iterate on curr.neighbors.
    if the original not in the map.. make the clone
    otherwise:
    put the cloned into the currCloned.neighbors
hm = {1:1', 2:2'}

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        stack = [node]
        hm = {}
        cloneNode = Node(node.val)
        hm[node] = cloneNode
        
        # 1:1'
        while stack:
            curr = stack.pop()  
            
            clonedNode = hm[curr]
            
            for n in curr.neighbors:
                if n not in hm:
                    copyN = Node(n.val)
                    hm[n] = copyN
                    stack.append(n)
                copyN = hm[n]
                clonedNode.neighbors.append(copyN)
        return hm[node]
                