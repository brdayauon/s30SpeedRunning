class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        n = len(s)
        dp =[[False for i in range(n)] for j in range(n)]
        
        self.mx = 0
        self.start = 0
        self.end = 0
        
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i-j <= 2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    if i-j+1 > self.mx:
                        self.mx = i-j+1
                        self.start = j
                        self.end = i
                        
        return s[self.start:self.end+1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        n = len(s)
        self.mx = float('-inf')
        self.start = 0
        for i in range(n):
            self.extendAroundPivot(s, i, i)
            if i < n-1 and s[i] == s[i+1]:
                self.extendAroundPivot(s, i, i+1)
        print(self.start, self.mx)
        return s[self.start:(self.start+self.mx)]
            
    
    def extendAroundPivot(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left - 1 > self.mx:
            self.mx = right - left - 1
            self.start = left + 1
             