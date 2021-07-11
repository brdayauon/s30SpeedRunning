class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = float('-inf')
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
           
            mx = max(mx, count)

        return mx