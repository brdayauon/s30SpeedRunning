# Time Complexity : O(n mlogm) N = number of elements in strs array and m is largest size a word in strs
# Space Complexity : O(N) number of elements in strs array
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        sort each individual element in strs and put it into hashmap...if the sorted part exists, just append the element 
        to existing/respective list. 

        put values into a returning array and return it... WORKS
        """
        res = [] 
        mapping = defaultdict(list)
        for i in range(len(strs)):
            charArr = sorted(strs[i])
            sortedWord = ''.join(charArr)
            if sortedWord not in mapping:
                mapping[sortedWord] = [strs[i]]
            else:
                mapping[sortedWord].append(strs[i])
        
        for i in mapping.values():
            res.append(i)
        
        return res