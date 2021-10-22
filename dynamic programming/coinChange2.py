class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def helper(coins, index, amount):
            if index == len(coins):
                return 0
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            choose = helper(coins, index, amount-coins[index])
            dontChoose = helper(coins, index+1, amount)
            
            return choose+dontChoose
        
        return helper(coins,0,amount)