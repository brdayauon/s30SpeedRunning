class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.res = []
        self.hm = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.backtrack(digits, 0, [])
        
        return self.res 
    
    def backtrack(self, digits, index, curr):
        if index == len(digits):
            self.res.append(''.join(curr))
            return
        
        indexDigit = digits[index]
        
        for letters in self.hm[indexDigit]:
            #action
            curr.append(letters)
            
            #recurse
            self.backtrack(digits, index+1, curr)
            
            #backtrack
            curr.pop(-1)
            

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #backtrack
        if not digits:
            return []
        self.res = []
        self.hm = { "2" : "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        self.backtrack(digits, 0, [])
        return self.res 
    
    def backtrack(self, digits, index, curr):
        if index == len(digits):
            self.res.append(''.join(curr))
            return 
        
        for letter in self.hm[digits[index]]:
            curr.append(letter)
            self.backtrack(digits, index+1, curr)
            curr.pop()
            
        