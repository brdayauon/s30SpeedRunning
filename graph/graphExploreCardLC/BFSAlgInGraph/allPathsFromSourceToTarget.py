class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        hm = defaultdict(set)
        
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                hm[i].add(graph[i][j])
        queue = deque([(0, [0])])
        n = len(graph)
        res = []
        while queue:
            curr, path = queue.popleft()
            
            if curr == n-1:
                queue.append(path)
            
            if curr in hm:
                neighbors = hm[curr]
                for neigh in neighbors:
                    if neigh == n-1:
                        res.append(path+[neigh])
                    else:
                        queue.append((neigh, path+[neigh]))
        return res