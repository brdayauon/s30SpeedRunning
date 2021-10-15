class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        rank = [1 for i in range(len(isConnected))]
        
        def find(n):
            res = n
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
            
        def union(n1,n2):
            #get the parent
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = len(isConnected)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    res -= union(i,j)
        return res