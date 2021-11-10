class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevPrice = prices[0]
        
        total = 0
        
        for current in range(1, len(prices)):
            if prices[current] > prevPrice:
                total += prices[current] - prevPrice
            
            prevPrice = prices[current]
        return total 