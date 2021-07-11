class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        mx = float('-inf')
        
        left = 0
        right = 0
        hm = {}
        
        while right < len(s):
            if s[right] not in hm:
                hm[s[right]] = 1
            else:
                hm[s[right]] += 1
          
            while len(hm) > 2:
                if s[left] in hm:
                    hm[s[left]] -= 1
                    if hm[s[left]] == 0:
                        del hm[s[left]]
                left += 1
                
            right += 1
            mx = max(mx, right-left)
        return mx
        
 