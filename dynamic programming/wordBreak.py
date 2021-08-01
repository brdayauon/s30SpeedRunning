class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        
        seen = set(wordDict)
        
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(len(dp)):
            for j in range(0, i):
                if dp[j] == True and s[j:i] in seen:
                    dp[i] = True
                    break
        return dp[-1]


"""
U - 
apple|pen|apple ["apple","pen"]
cats|and|og ["cats","dog","sand","and","cat"]
cat|sand|og
​
M- recursive --> dp
P- go through string
    check if its in wordDict (valid word)
    
"""
​
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        self.seen = set(wordDict)
        return self.helper(s)
    
    def helper(self, s):
        #base 
        if len(s) == 0:
            return True
        #logic
        for i in range(len(s)):
            if s[0:i+1] in self.seen and self.helper(s[i+1:]):
                return True
        return False