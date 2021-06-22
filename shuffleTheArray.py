class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #just do two pointers left and one at mid. then add to list
        left = 0
        mid = len(nums) //2
        res = []
        while mid < len(nums):
            res.append(nums[left])
            res.append(nums[mid])
            left += 1
            mid += 1
        return res            