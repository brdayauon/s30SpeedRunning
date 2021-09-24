#O(len(coins)*len(amount))
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for i in range(amount+1)] for i in range(len(coins)+1)]
        
        for i in range(len(dp[0])):
            dp[0][i] = amount+1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    #                        j=current amt u are on - denomination of the coin
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j- coins[i-1]])
                    
        res = dp[-1][-1]
        if res >= amount+1:
            return -1
        return res

#RECURSION
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0
        return self.helper(coins, 0, amount, 0)
    
    def helper(self, coins, index, amount, totalCoins):
        if index == len(coins):
            return -1
        if amount == 0:
            return totalCoins
        elif amount < 0:
            return -1
        
        #choose
        case1 = self.helper(coins, index, amount-coins[index], totalCoins+1)
        #not choose
        case2 = self.helper(coins, index+1, amount, totalCoins)
        if case1 == -1:
            return case2
        if case2 == -1:
            return case1
        return min(case1, case2)