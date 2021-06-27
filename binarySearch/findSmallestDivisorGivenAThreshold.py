class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # optimal O(nlgn)
        def totalSumLessThanEqualToThreshold(divisor):
            totalSum = 0
            for i in range(len(nums)):
                totalSum += math.ceil(nums[i] / divisor)
            
            if totalSum <= threshold:
                return True
            return False
                
            
        left = 1
        right = max(nums)
        while left < right:
            middle = left + (right-left) // 2
            
            if totalSumLessThanEqualToThreshold(middle):
                right = middle
            else:
                left = middle + 1
        return right
        
#         #brute force n^2
#         n = max(nums)
#         for i in range(1,n):
#             totalSum = 0
#             for j in range(len(nums)):
#                 totalSum += math.ceil(nums[j] / i)
            
#             if totalSum <= threshold:
#                 return i
                    
#         return n