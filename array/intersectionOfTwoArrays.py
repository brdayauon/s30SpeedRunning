class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        res = set()
        
        for i in range(len(nums2)):
            if nums2[i] in seen:
                res.add(nums2[i])
                
        return res