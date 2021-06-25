class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        hm = {} # {runningSum : occurrence}
        count = 0
        runningSum = 0
        #initialize
        hm[0] = 1
        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum - k in hm:
                count += hm[runningSum-k]
                
            if runningSum not in hm:
                hm[runningSum] = 1
            else:
                hm[runningSum] += 1
                
            
        return count