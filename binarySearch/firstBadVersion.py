"""
TC: O(logN)
SC: O(1)
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        
        while left < right:
            middle = left + (right-left)//2
            
            if not isBadVersion(middle):
                left = middle + 1
            elif isBadVersion(middle):
                right = middle
                
        return right