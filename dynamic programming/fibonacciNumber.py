class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0 for i in range(n)]
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]
    