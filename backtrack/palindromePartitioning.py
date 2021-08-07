class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.backtrack(s, 0, [])
        return self.res 
    
    def backtrack(self, s, index, path):
        #base
        if index == len(s):
            self.res.append(list(path))
            return
        #logic
        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                path.append(s[index:i+1])
                self.backtrack(s, i+1, path)
                path.pop()
        
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True