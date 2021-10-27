class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end:
            return True
        
        hm = defaultdict(set)
        stack = []
        seen = set()
        
        for edge in edges:
            hm[edge[0]].add(edge[1])
            hm[edge[1]].add(edge[0])
        
        stack = [start]
        seen.add(start)
        
        while stack:
            curr = stack.pop()
            if curr == end:
                return True
            if curr in hm:
                neighbors = hm[curr]
                for n in neighbors:
                    if n not in seen:
                        if n == end:
                            return True
                        stack.append(n)
                        seen.add(n)
        return False
                