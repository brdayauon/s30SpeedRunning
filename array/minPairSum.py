class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        left = 0 
        right = len(nums)-1
        mx = float('-inf')
        while left < right:
            mx = max(mx, nums[left]+nums[right])
            left += 1
            right -= 1
        return mx
    
s = Solution()

a = [-6,-5]
b = [2,2,2,2,2,2]
c = []
print(s.minPairSum(a))
print(s.minPairSum(b))
print(s.minPairSum(c))
print(s.minPairSum(d))