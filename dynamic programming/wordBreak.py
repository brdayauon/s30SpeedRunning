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