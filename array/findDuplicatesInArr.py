class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        seen = set()
        res = []
        for num in nums:
            if num in seen:
                res.append(num)
            seen.add(num)
        return res