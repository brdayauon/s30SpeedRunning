class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        n = len(nums)
        for i in range(len(nums)):
            seen.add(nums[i])
            
        res = []
        for i in range(1,n+1):
            if i not in seen:
                res.append(i)
                
        return res