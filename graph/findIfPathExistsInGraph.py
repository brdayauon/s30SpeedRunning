class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end:
            return True
        from collections import defaultdict
        hm = defaultdict(set)
        
        for edge in edges:
            hm[edge[0]].add(edge[1])
            hm[edge[1]].add(edge[0])
        queue = deque([start])
        seen = set()
        while queue:
            curr = queue.popleft()
            
            for neighbors in hm[curr]:
                if neighbors not in seen:
                    queue.append(neighbors)
                if neighbors == end:
                    return True
                seen.add(neighbors)
        return False