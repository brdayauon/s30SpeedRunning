# DFS SOLUTION
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        
        #create adjacency list
        hm = {}
        for i in range(len(graph)):
            if i not in hm:
                hm[i] = []
            for j in range(len(graph[i])):
                hm[i].append(graph[i][j])

        self.res = []
        
        def dfs(hm, start, end, path):
            if start == end:
                self.res.append(path)
                return
            for edges in hm[start]:
                dfs(hm,edges,end, path + [edges])
                
        dfs(hm, 0, len(graph)-1, [0])
        
        return self.resd