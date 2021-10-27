class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end:
            return True
        hm = defaultdict(set)
        
        for edge in edges:
            hm[edge[0]].add(edge[1])
            hm[edge[1]].add(edge[0])
        
        if start not in hm:
            return False
        
        queue = deque([start])
        seen = set()
        seen.add(start)
        
        while queue:
            curr = queue.popleft()
            if curr == end:
                return True
            if curr in hm:
                neighbors = hm[curr]
                
                for n in neighbors:
                    if n not in seen:
                        if n == end:
                            return True
                        seen.add(n)
                        queue.append(n)
                    
        return False
                    
                    
                    
                    
            
            