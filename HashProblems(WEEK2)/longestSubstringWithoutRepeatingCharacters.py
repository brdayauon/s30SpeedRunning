class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        
        hm = {}
        mx = 0
        while right < len(s):
            if s[right] not in hm:
                hm[s[right]] = 1
            else:
                hm[s[right]] += 1
            
            mx = max(len(hm), mx)
            while hm[s[right]] > 1:
                hm[s[left]] -= 1
                if hm[s[left]] == 0:
                    del hm[s[left]]
                left += 1
                
            right += 1
        return mx