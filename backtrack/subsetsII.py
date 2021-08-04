class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums = sorted(nums)
        self.backtrack(nums, 0, [])
        return self.res 
    
    def backtrack(self, nums, index, curr):
        if curr not in self.res:
            self.res.append(list(curr))
        
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.backtrack(nums, i+1, curr)
            curr.pop()