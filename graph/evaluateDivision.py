from collections import defaultdict 
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #build adjacency matrix
        hm = defaultdict(set)
        for i in range(len(equations)):
            x,y = equations[i]
            hm[x].add((y,values[i]))
            hm[y].add((x, 1/values[i]))
            
        res = []
        for pair in queries:
            reachEnd = False
            start,end = pair
            queue = deque([(start, 1)])
            visited = set()
            
            if start not in hm or end not in hm:
                res.append(-1)
                continue
            while queue:
                curr, currVal = queue.popleft()
                if curr == end:
                    reachEnd = True
                    res.append(currVal)
                    continue
                neighbors = hm[curr]
                for n in neighbors:
                    if n[0] not in visited:
                        visited.add(n[0])
                        queue.append((n[0], currVal*n[1]))
            if reachEnd == False:
                res.append(-1)
        return res
    