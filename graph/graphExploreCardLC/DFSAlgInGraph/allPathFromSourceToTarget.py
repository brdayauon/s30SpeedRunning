"""
this question we start at node 0 and need to get to the last node.. given list of edges how can we get to there?

#create adjacency list  O(N)

#use a stack becuz DFS (put in curr node and curr path).. 

"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        hm = defaultdict(set)
        
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                hm[i].add(graph[i][j])
                
        stack = [(0, [0])]
        res = []
        
        while stack:
            curr, path = stack.pop()
            if curr == len(graph)-1:
                res.append(path)
                
            neighbors = hm[curr]
            for n in neighbors:
                    stack.append((n, path+[n]))
        return res