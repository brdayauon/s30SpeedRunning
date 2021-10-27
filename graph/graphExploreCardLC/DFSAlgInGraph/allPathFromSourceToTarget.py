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