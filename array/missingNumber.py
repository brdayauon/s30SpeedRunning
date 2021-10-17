class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        expected = 0
        for i in range(0,len(nums)+1):
            expected += i
        return expected-total