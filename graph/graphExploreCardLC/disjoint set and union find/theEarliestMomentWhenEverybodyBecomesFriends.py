""" 
logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6

rank = [1, 1, 1, 1, 1]
parents = [0,0,2,3,4,5]

"""

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def find(x):
            res = x
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
            
            
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2:
                return 0
            
            if p1 < p2:
                parent[p1] = p2
                rank[p1] += rank[p2]
            elif p1 > p2:
                parent[p2] = p1
                rank[p2] += rank[p1]
            return 1
        total = n-1
        logs.sort()
        for log in logs:
            time, person1, person2 = log
            if union(person1,person2) == 1:
                total -= 1
            if total == 0:
                return time
        return -1