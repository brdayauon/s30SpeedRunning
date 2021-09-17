class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+2)
        
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], nums[i-2]+dp[i-2])
            
        return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.helper(nums, 0, 0)
        
    def helper(self, nums, index, total):
        if index > len(nums)-1:
            return total
        #choose
        choose1 = nums[index] + self.helper(nums, index+2, total)
        #not choose
        choose2 = self.helper(nums, index+1, total)
        
        return max(choose1, choose2)