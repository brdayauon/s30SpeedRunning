class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(nums, start, path): 
             
            if len(path) == len(nums):
                res.append(list(path))
                return 
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums, i, path)
                path.pop()
                
        backtrack(nums, 0, [])
        
        return res