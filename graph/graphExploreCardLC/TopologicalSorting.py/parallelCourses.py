class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = [0 for i in range(n+1)]
        hm = defaultdict(set)
        
        for relation in relations:
            hm[relation[0]].add(relation[1])
            indegree[relation[1]] += 1
        
        queue = deque([])
        
        for i in range(1,len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        
        while queue:
            size = len(queue)
            count += 1
            for i in range(size):
                curr = queue.popleft()
                
                if curr in hm:
                    neighbors = hm[curr]
                    
                    for n in neighbors:
                        indegree[n] -= 1
                        if indegree[n] == 0:
                            queue.append(n)
        
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return -1
        return count