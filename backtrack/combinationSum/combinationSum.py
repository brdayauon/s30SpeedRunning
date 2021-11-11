class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(candidates, index, target, path):
            if target < 0:
                return 
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(candidates, i, target-candidates[i], path)
                path.pop()
            
        backtrack(candidates, 0, target, [])
        
        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(candidates, index, target, path):
            if target < 0:
                return 
            
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(candidates, i+1, target-candidates[i], path)
                path.pop()
        candidates.sort() 
        backtrack(candidates, 0, target, [])
        return res
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
         
        def backtrack(target, k, path, start):
            if target < 0 or len(path) > k:
                return
            if target == 0 and len(path) == k:
                res.append(list(path))
            
            for i in range(start, 10):
                path.append(i)
                backtrack(target-i, k, path, i+1)
                path.pop()
                
        backtrack(n, k, [], 1)
        return res