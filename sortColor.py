class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        3 pointers. left right and middle
        """
        left = mid = 0
        right = len(nums)-1
        
        while mid <= right: 
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                #swap with the right pointer and move right pointer down 1 and increase mid
                self.swap(nums,mid,right)
                right -= 1
            else:
                #swap with the left pointer and move left pointer up 1 and increase mid
                self.swap(nums, mid, left)
                left += 1 
                mid += 1
        
                
    def swap(self, nums, p1, p2):
        temp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = temp
        
        