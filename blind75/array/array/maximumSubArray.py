class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mx = float('-inf')
        total = 0
        for i in range(len(nums)):
            
            #get running sum 
            total += nums[i]
            
            #update mx
            if mx < total:
                mx = total
            
            #if running sum is less than 0 reset the total
            if total < 0:
                total = 0
                
        return mx