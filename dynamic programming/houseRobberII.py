class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max((nums))
         
        return max(self.robInterval(nums,0, len(nums)-1), self.robInterval(nums, 1, len(nums)))
        
        
    def robInterval(self, nums, left, right):
        prev = 0
        curr = nums[left]
        
        for i in range(left+1, right):
            temp = prev 
            prev = max(prev, curr)
            curr = temp+nums[i]
        return max(prev, curr)