class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        total = 0
        for k,v in count.items():
            if v == 1:
                total += k
        return total