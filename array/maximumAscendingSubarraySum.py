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