class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while left < right:
            middle = left + (right-left)//2
            
            if (nums[middle] < nums[middle-1]) and nums[middle] < nums[middle+1]:
                return nums[middle]
            elif nums[middle] < nums[right]:
                right = middle-1
                #left = middle + 1
            else:
                left = middle + 1
                #right = middle-1
                
        return nums[left]