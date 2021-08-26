class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        if len(edges) != n-1:
            return False
        hm = defaultdict(set)
        
        for edge in edges:
            hm[edge[0]].add(edge[1])
            hm[edge[1]].add(edge[0])
            
        seen = set()
        
        queue = deque([0])
        seen.add(0)
        while queue:
            curr = queue.popleft()
            
            if curr in hm:
                neighbors = hm[curr]
                for neigh in neighbors:
                    if neigh in seen:
                        continue
                    queue.append(neigh)
                    seen.add(neigh)
        return len(seen) == n