class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0, [])
        
        return self.res
    
    
    def backtrack(self, nums, index, curr):
        self.res.append(list(curr))
        
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.backtrack(nums, i+1, curr)
            curr.pop()