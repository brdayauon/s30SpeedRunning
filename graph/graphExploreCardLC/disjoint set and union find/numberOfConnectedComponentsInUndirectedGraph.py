class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        #gets the root/parent
        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1,n2):
            #get the root/parent for each node 
            p1 = find(n1)
            p2 = find(n2)
            
            #have the same parent already connected
            if p1 == p2:
                return 0
            #diff parents if p2 ranks higher than p1.. set the parent of p1 to p2. and increase the rank
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)
        return res