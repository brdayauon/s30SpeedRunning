class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx = float('-inf')
        total = 0
        total += nums[0]
        mx = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                total += nums[i]
            else:
                total = nums[i]
            mx = max(mx, total)
        return mx

#10.24 solution
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx = nums[0]
        
        prev = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += nums[i]
            else:
                curr = nums[i]
            mx = max(mx, curr)
        return mx