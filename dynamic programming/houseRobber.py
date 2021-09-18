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

#CHOOSE NOT CHOOOSE BUT IN VARIABLES. 
"""     0   1
    --------------
2   |   0   2
7   |   2   0+7 
9   |   7   2+9
8   |   11  7+8
1   |   15   12
    choose max^
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) < 2:
        #     return nums[0]
        prev = 0
        curr = nums[0]
        
        for i in range(1, len(nums)):
            temp = prev
            prev = max(prev, curr)
            curr = temp + nums[i]
        
        return max(prev,curr)