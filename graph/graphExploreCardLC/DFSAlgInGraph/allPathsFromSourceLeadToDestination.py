# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/discuss/1421577/Java-or-DFS-or-Cycle-detection-or-Modified-traversal
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hm = defaultdict(set)
        for edge in edges:
            hm[edge[0]].add(edge[1])
        self.seen = set()
        if len(hm[destination]) > 0:
            return False
        def dfs(starting, destination):
            if starting == destination:
                return True
                    
            neighbor = hm[starting]
            if len(neighbor) == 0:
                return False
            
            self.seen.add(starting)
            for n in neighbor:
                if n in self.seen:
                    return False
                if not dfs(n, destination):
                    return False
            
            #backtrack
            self.seen.remove(starting)
            return True
            
        return dfs(source,destination)
