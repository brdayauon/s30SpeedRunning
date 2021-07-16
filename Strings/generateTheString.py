class Solution:
    def generateTheString(self, n: int) -> str:
        res = []
        
        if n % 2 != 0:
            for i in range(n):
                res.append('a')
            return res
        
        else:
            for i in range(n-1):
                res.append('a')
            res.append('b')
            return ''.join(res)