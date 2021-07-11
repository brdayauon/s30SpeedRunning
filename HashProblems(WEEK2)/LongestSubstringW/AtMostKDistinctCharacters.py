class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        mx = float('-inf')
        
        left = 0
        right = 0
        hm = {}
        
        while right < len(s):
            if s[right] not in hm:
                hm[s[right]] = 1
            else:
                hm[s[right]] += 1
          
            while len(hm) > k:
                if s[left] in hm:
                    hm[s[left]] -= 1
                    if hm[s[left]] == 0:
                        del hm[s[left]]
                left += 1
                
            right += 1
            mx = max(mx, right-left)
        return mx