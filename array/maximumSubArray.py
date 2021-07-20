class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float('-inf')
        total = 0
        left = 0
        right = 0
        s = 0 #s is more like a new start
        for i in range(len(nums)):
            total += nums[i]
            
            # mx = max(total, mx) #when we change max is when theres a new start/end position
            if mx < total:
                mx = total 
                left = s
                right = i
            if total < 0:
                total = 0
                s = i+1
        
        res = []
        for i in range(left,right+1):
            res.append(nums[i])
        return mx