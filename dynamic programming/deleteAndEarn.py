"""
TC: O(N) -> size of dp
SC: O(N) N->size of dp

So in delete and earn.. we are given array of nums where each nums is a point. When we choose a point the point+1 and point-1 are deleted.
To do this we count up all the values into an array from their index.
Ex: [1,2,2,3,1,2]
    [0,2,6,3] ->Then the best thing to choose is 2s

    Essentially its reduced to house robber problem
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mx = max(nums)
        dp = [0 for i in range(mx+1)]
        for i in range(len(nums)):
            dp[nums[i]] += nums[i]
        notChoose = 0
        choose = 0
        for i in range(len(dp)):
            if notChoose == 0 and choose == 0:
                notChoose = 0
                choose = notChoose + dp[i]
            else:
                temp = notChoose
                notChoose = max(notChoose, choose)
                choose = temp + dp[i]
                
        return max(choose,notChoose)