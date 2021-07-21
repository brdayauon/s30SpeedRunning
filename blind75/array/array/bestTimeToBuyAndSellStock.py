class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        prev = prices[0]
        mx = 0
        
        for i in range(1,len(prices)):
            if prices[i] < prev:
                prev = prices[i]
            else:
                mx = max(prices[i]-prev, mx)
            
        return mx