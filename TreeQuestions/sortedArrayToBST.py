# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(nums, left, right):
            middle = left + (right-left)//2

            root = TreeNode(nums[middle])
            if right < left:
                return None
        
            
            root.left = helper(nums, left, middle-1)
            root.right = helper(nums,middle+1, right)
            
            return root
        
        return helper(nums,0, len(nums)-1)