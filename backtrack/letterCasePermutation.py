class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res = []
        
        self.backtrack(s, 0, [])
        
        return self.res
    
    def backtrack(self, s, index, curr):
        if len(curr) == len(s):
            self.res.append(''.join(curr))
        
        for i in range(index, len(s)):
            if not s[index].isalpha():
                curr.append(s[index])
                self.backtrack(s, i+1, curr)
                curr.pop()
                
            else:
                curr.append(s[index].upper())
                self.backtrack(s, i+1, curr)
                curr.pop()
                
                curr.append(s[index].lower())
                self.backtrack(s, i+1, curr)
                curr.pop()