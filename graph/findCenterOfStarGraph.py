class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        degree = [0 for i in range(n)]
        for edge in edges:
            num1 = edge[0]-1
            num2 = edge[1]-1
            
            degree[num1] += 1
            degree[num2] += 1
        
        for i in range(len(degree)):
            if degree[i] == n-1:
                return i + 1
            
        return -1