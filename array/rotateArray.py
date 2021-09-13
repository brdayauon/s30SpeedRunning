"""
O(1) SPACE WAY
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums,k, len(nums)-1)
        
    def reverse(self, nums, left, right):
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

"""
O(N) SPACE
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        n = (n-k)%n
        res = []
        
        for i in range(n, len(nums)):
            res.append(nums[i])
            
        for i in range(0, n):
            res.append(nums[i])
        
        for i in range(len(nums)):
            nums[i] = res[i]
        
        