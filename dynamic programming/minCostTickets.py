"""
TC: O(N)
SC: O(N)
Create an array size of max number of days+1. with element 0
Do a loop from 1 -> the last days and store values accordingly. 
    - If i is not within days.. then keep the value as the same in the previous index. 
    - if it is.. calculate the min amount needed up to that point.
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        mx = max(days)
        days = set(days)
        dp = [0 for i in range(mx+1)]
        
        for i in range(1, len(dp)):
            if i in days:
                dp[i] = min(dp[i-1]+costs[0],
                            dp[max(i-7,0)]+costs[1],
                            dp[max(i-30,0)]+costs[2]
                           )
            else:
                dp[i] = dp[i-1]
        return dp[-1]