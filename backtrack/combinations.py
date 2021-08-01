class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.k = k
        self.backtrack(n, 1, [])
        return self.res 
    
    def backtrack(self, n, index, curr):
        if len(curr) == self.k:
            self.res.append(list(curr))
            return
            
        for i in range(index, n+1):
            curr.append(i)
            self.backtrack(n, i+1, curr)
            curr.pop()