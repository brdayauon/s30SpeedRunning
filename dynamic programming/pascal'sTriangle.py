"""
   i=0  1
        1 1
        1 2 1
        1 3 3 1
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            curr = []
            for j in range(i+1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    right = res[i-1][j]
                    left = res[i-1][j-1]
                    curr.append(left+right)
            res.append(curr)
        return res
    
