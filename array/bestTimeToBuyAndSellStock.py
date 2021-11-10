class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentLowest = prices[0]
        total = 0
        
        for currPrice in range(1, len(prices)):
            if prices[currPrice] < currentLowest:
                currentLowest = prices[currPrice]
            else:
                total = max(total, prices[currPrice]-currentLowest)
        return total