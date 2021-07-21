class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        if not nums:
            return res
        
        rp = 1
        num = 1
        for i in range(1,len(nums)): # [1,1,2,6] gets the running product up to that index
            rp = rp * nums[i-1]
            res[i] = rp
            
        rp = 1
        for i in range(len(nums)-2,-1,-1):
            rp = rp * nums[i+1]
            res[i] = rp * res[i]
        
        return res