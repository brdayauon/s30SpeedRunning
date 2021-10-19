"""
TC: O(nLgN) -> due to sorting
SC:  O(N) using extra array if using sorted(nums) O(1) if using nums.sort()
Given an array of nums and a k value.. find a pair where pair(i,j) i < j and the values of i,j is == k. 
Can do brute force with two for loops. 
Another way is to sort the values. 
have a left/right pointer initialized to 0
Then we do a while loop until i or j goes outta bounds. 
    - make sure i and j aren't pointing at the same thing.. if they are increase j+1 and continue to next loop
    - if the values of i,j is == k.. then increase the total and move the two pointers by 1.. (or the right pointer rathere)
        - make sure the pointers arent equal to the index before. 
    - elif the difference < k... increase right pointer
    - else the difference > k.. increase the left pointer
"""
# moving only right pointer
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        right = 0
        total = 0
        
        while right < len(nums) and left < len(nums):
            if left == right:
                right += 1
                continue
            check = abs(nums[left]-nums[right]) 
            if check == k:
                total += 1
                left += 1
                right += 1
    
                while right < len(nums) and nums[right] == nums[right-1]:
                    right += 1
            elif check < k:
                right += 1
            else:
                left += 1
        return total
#moving left and right pointers ... includes extra if statement check
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        right = 0
        total = 0
        
        while right < len(nums) and left < len(nums):
            if left == right:
                right += 1
            if right >= len(nums) or left >= len(nums):
                break
            check = abs(nums[left]-nums[right]) 
            if check == k:
                total += 1
                left += 1
                right += 1
                while left < len(nums) and nums[left] == nums[left-1]:
                    left += 1
                while right < len(nums) and nums[right] == nums[right-1]:
                    right += 1
            elif check < k:
                right += 1
            else:
                left += 1
        return total