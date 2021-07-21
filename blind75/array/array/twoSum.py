class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {} #{ complement: index }
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in hm:
                hm[nums[i]] = i
            else:
                return [i, hm[complement]]
            