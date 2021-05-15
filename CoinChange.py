class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #recursive
        return self.helper(coins, amount, 0, 0)
    
    def helper(self, coins, remainingAmount, index, numberOfCoins):
        #base case if the remainingAmt is < 0 or coins outta range
        if remainingAmount < 0 or index > len(coins)-1:
            return -1
        #hit a valid leaf
        if remainingAmount == 0:
            return numberOfCoins
        #choose
        numberOfCoins1 = self.helper(coins, remainingAmount-coins[index], index, numberOfCoins+1)
        #not choose
        numberOfCoins2 = self.helper(coins, remainingAmount, index+1, numberOfCoins)
        
        if numberOfCoins1 == -1:
            return numberOfCoins2
        if numberOfCoins2 == -1:
            return numberOfCoins1
        
        return min(numberOfCoins1, numberOfCoins2)