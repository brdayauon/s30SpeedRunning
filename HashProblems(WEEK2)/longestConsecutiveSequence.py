class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mn = float('inf')
        mx = float('-inf')
        hm = {}
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                continue
            mn = min(mn, nums[i])
            mx = max(mx, nums[i])
        count = 0
        longestSequence = float('-inf')
        
        for key,val in hm.items():
            if key-1 not in hm:
                count = 0
                temp = key
                while temp in hm:
                    count += 1
                    temp += 1
                longestSequence = max(longestSequence, count)
        # for i in range(mn, mx+1):
        #     if i not in hm:
        #         count = 0
        #     else:
        #         count += 1
        #         longestSequence = max(count, longestSequence)
        return longestSequence