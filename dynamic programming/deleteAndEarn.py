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