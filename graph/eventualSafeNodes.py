#DFS
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        hm = {}
        
        #create adjacency list .. of indegree? { 0 : 3} 3 points to 0
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] not in hm:
                    hm[graph[i][j]] = []
                hm[graph[i][j]].append(i)
                
        degree = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                degree[i] += 1
        
        queue = deque([])
        stack = []
        for i in range(len(degree)):
            if degree[i] == 0:
                stack.append(i)
        
        while stack:
            curr = stack.pop() 
            if curr in hm:
                neigh = hm[curr]

                for n in neigh:
                    degree[n] -= 1
                    if degree[n] == 0:
                        stack.append(n)
        res = []
        for i in range(len(degree)):
            if degree[i] == 0:
                res.append(i)
        return res



#BFS
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        hm = {}
        
        #create adjacency list .. of indegree? { 0 : 3} 3 points to 0
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] not in hm:
                    hm[graph[i][j]] = []
                hm[graph[i][j]].append(i)
                
        degree = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                degree[i] += 1
        
        queue = deque([])
    
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft() 
            if curr in hm:
                neigh = hm[curr]

                for n in neigh:
                    degree[n] -= 1
                    if degree[n] == 0:
                        queue.append(n)
        res = []
        for i in range(len(degree)):
            if degree[i] == 0:
                res.append(i)
        return res
