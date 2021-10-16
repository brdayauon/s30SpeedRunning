"""  
Basically... we start at the given node... and build as we go.
What we do is do a bfs/dfs to traverse the graph. Start off by creating the copy.
We do this by creating an Original:Copy hashmap.
Now we process the stack/queue.
We pop and go through the neighbors. 
    - issue here is that we need to check if if the original Neighbor is in the hashmap.. if it is not we need to create that cloned copy so we can append it as a neighbor.
        - when n is not in the hm.. then we append it to the queue. 
    - at this point we just append the clonedNeighbors to the clone.
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
        queue = deque([node])
        hm = {}
        cloneNode = Node(node.val)
        hm[node] = cloneNode
        
        while queue:
            curr = queue.popleft()
            for n in curr.neighbors:
                if n not in hm:
                    hm[n] = Node(n.val)
                    queue.append(n)
                hm[curr].neighbors.append(hm[n])
        return hm[node]