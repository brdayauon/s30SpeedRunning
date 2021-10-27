class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        rank = [1 for i in range(n+1)]
        
        def find(n):
            res = n
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2:
                return 0
            if rank[p2] >= rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        edges = pipes
        for i in range(len(wells)):
            edges.append([0,i+1,wells[i]])
        
        edges = sorted(edges, key=lambda x: x[2])
        
        total = 0
        for edge in edges:
            n1, n2, cost = edge
            if union(n1,n2) == 1:
                total += cost
        return total
        