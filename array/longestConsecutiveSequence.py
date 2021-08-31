class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        count = 0
        mx = float('-inf')
        for i in seen:
            if i+1  not in seen:
                count = 0
                temp = i
                while temp in seen:
                    count += 1
                    temp -= 1

                mx = max(mx, count)
        return mx