class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums)-1
        mx = float('-inf')
        while left < right:
            if nums[left]+nums[right] < k:
                mx = max(mx, nums[left]+nums[right])
                left += 1
            elif nums[left]+nums[right] >= k:
                right -= 1
            else:
                left += 1
            
        
        return mx if mx != float('-inf') else -1