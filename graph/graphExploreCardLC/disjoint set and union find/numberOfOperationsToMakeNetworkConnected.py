class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2: #already unioned
                return 0
            
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        def find(n):
            res = parent[n]
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        if len(connections) < n-1:
            return -1
        res = n-1
        for connection in connections:
            if union(connection[0],connection[1]) == 1:
                res -= 1
    
        #for i in range(len(parent)):
            
        return res