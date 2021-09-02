class Solution:
    def arraySign(self, nums: List[int]) -> int:
        rProd = nums[0]
        
        for i in range(1, len(nums)):
            rProd *= nums[i]
        
        if rProd > 0:
            return 1
        elif rProd < 0:
            return -1
        else:
            return 0