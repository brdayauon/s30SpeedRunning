class Solution:
    def totalMoney(self, n: int) -> int:
        #TC: O(n) SC: O(n)
        dp = [0 for i in range(n)]
        
        dp[0] = 1
        growth = 1
        
        for i in range(1, len(dp)):
            if i % 7 == 0:
                dp[i] = dp[i-7] + 1
            else:
                dp[i] = dp[i-1] + 1
        return sum(dp)
# class Solution:
#     def totalMoney(self, n: int) -> int:
#         startGrowth = growth = prevGrowth = 1
#         total = 0
#         for i in range(n):
#             if i % 7 == 0:
#                 startGrowth += 1
#                 growth = startGrowth
            
#             prevGrowth = growth
#             total += growth + 1
#             growth += 1
#             print(total)
            
#         return total