""" 
    a   e   i  o  u
1   1   1   1  1  1
2   5   4   3  2  1         <- the sum at dp[i][j] is the previous row from j till the end
3   15  10  6  3  1

Optimization can be change from matrix DP to 1 arr.by getting the running sum
"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for vowels in range(5)] for rows in range(n)]
        for i in range(len(dp[0])):
            dp[0][i] = 1
        for i in range(1,len(dp)):
            for j in range(len(dp[i])):
                if j != 4:
                    dp[i][j] = sum(dp[i-1][j:])
                else:
                    dp[i][j] = 1
        return sum(dp[-1])