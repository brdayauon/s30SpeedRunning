class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        degree = [0 for i in range(len(graph))]
        res = deque([])
        queue = deque([])
        
        #need in degree
        from collections import defaultdict as dd
        hm = dd(set)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                hm[graph[i][j]].add(i)
        
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                degree[i] += 1
            
            if degree[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in hm[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return sorted(res)
         