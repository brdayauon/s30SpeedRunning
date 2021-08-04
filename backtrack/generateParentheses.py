"""
U - generate parentheses (all must be legit)

M- Backtracking

P - 
 n = 2
 (( )) -increased left by two then starting increasing right
 ()() -
                 []             [(, (,]
                /   
              [(]
              /  \
            [((]  [()]  
 1,2,5
    - keep track of open and closing parentheses
    
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.res = []
                    #array, path, index
        self.backtrack(n, [], 0, 0)
        
        return self.res 
    
    def backtrack(self, n, path, left, right):
        if len(path) == 2*n:
            self.res.append(''.join(path))
            return
        
        #when do we put open/left
        if left < n:
            path.append('(')
            self.backtrack(n, path, left+1, right)
            path.pop()
        #we close when there is a left
        if right < left:
            path.append(')')
            self.backtrack(n, path, left, right+1)
            path.pop()
        