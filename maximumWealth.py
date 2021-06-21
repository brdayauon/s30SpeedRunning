class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = float('-inf')
        if not accounts:
            return mx
        for i in range(len(accounts)):
            customerTotal = 0
            for j in range(len(accounts[i])):
                customerTotal += accounts[i][j]
            mx = max(mx, customerTotal)
        return mx