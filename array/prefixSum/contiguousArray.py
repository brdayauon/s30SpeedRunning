class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        rSum = 0
        hm = {}
        mxLength = 0
        #hm[0] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                rSum -= 1
            else:
                rSum += 1
            if rSum == 0:
                mxLength = max(mxLength, i+1)
            if rSum not in hm:
                hm[rSum] = i
            else:
                mxLength = max(mxLength, i - hm[rSum])
        # if nums[len(nums)-1] == 1:
        #     rSum += 1
        # else:
        #     rSum -= 1
        # if rSum in hm:
        #     mxLength = max(mxLength, len(nums)-hm[rSum])
        return mxLength